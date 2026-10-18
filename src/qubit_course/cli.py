"""Run one experiment or the complete course, saving auditable artifacts."""
import argparse
from datetime import datetime, timezone
import importlib.metadata
import json
from pathlib import Path
import platform
import subprocess
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from .experiments import EXPERIMENTS


def run(name, seed, output):
    folder = Path(output) / name
    folder.mkdir(parents=True, exist_ok=True)
    if (folder / 'metrics.json').exists():
        raise FileExistsError(f'Existing run in {folder}; choose a new --output directory.')
    start = time.perf_counter()
    metrics, arrays = EXPERIMENTS[name](seed)
    metrics['wall_seconds'] = time.perf_counter() - start
    metrics['seed'] = seed
    try:
        repo = Path(__file__).resolve().parents[2]
        commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo,
                                         stderr=subprocess.DEVNULL, text=True).strip()
        dirty = bool(subprocess.check_output(['git', 'status', '--porcelain'], cwd=repo, text=True).strip())
    except (OSError, subprocess.CalledProcessError):
        commit = None
        dirty = None
    metadata = {'utc': datetime.now(timezone.utc).isoformat(), 'experiment': name,
                'python': platform.python_version(), 'platform': platform.platform(),
                'source_commit': commit, 'working_tree_dirty': dirty,
                'versions': {p: importlib.metadata.version(p) for p in ['qutip', 'numpy', 'scipy', 'matplotlib']},
                'units': {'time': 'microsecond', 'angular_frequency': 'radian/microsecond', 'hbar': 1},
                'solver': {'atol': 1e-10, 'rtol': 1e-10} if name in ['rabi', 'noise', 'leakage'] else None}
    np.savez_compressed(folder / 'arrays.npz', **arrays)
    (folder / 'metrics.json').write_text(json.dumps(metrics, indent=2, allow_nan=False), encoding='utf-8')
    (folder / 'metadata.json').write_text(json.dumps(metadata, indent=2), encoding='utf-8')
    fig, ax = plt.subplots(figsize=(7, 4))
    if 'time_us' in arrays:
        for key, value in arrays.items():
            if key != 'time_us' and np.asarray(value).shape == arrays['time_us'].shape:
                ax.plot(arrays['time_us'], value, label=key)
        ax.set_xlabel('Time (microseconds)')
        ax.set_ylabel('Probability / expectation')
        ax.legend()
    elif 'pulse_xy' in arrays:
        times = np.arange(len(arrays['pulse_xy']) + 1) / len(arrays['pulse_xy'])
        ax.step(times, np.r_[arrays['pulse_xy'][:, 0], arrays['pulse_xy'][-1, 0]], where='post', label='X')
        ax.step(times, np.r_[arrays['pulse_xy'][:, 1], arrays['pulse_xy'][-1, 1]], where='post', label='Y')
        ax.set_xlabel('Slot start (microseconds)')
        ax.set_ylabel('Amplitude (rad/microsecond)')
        ax.legend()
    elif 'probabilities' in arrays:
        ax.bar(np.arange(len(arrays['probabilities'])), arrays['probabilities'])
        ax.set_xlabel('Basis-state index (MSB-first)')
        ax.set_ylabel('Probability')
    else:
        real_metrics = {k: v for k, v in metrics.items() if isinstance(v, (int, float)) and k not in ['seed', 'wall_seconds']}
        ax.barh(list(real_metrics), list(real_metrics.values()))
        ax.set_xlabel('Value (see metrics.json for definitions)')
    ax.set_title(name.capitalize())
    fig.tight_layout()
    fig.savefig(folder / 'figure.png', dpi=160)
    plt.close(fig)
    print(f'{name}: {folder / "metrics.json"}')
    return metrics


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment', choices=[*EXPERIMENTS, 'all'])
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--output', default='runs/demo')
    args = parser.parse_args()
    for name in EXPERIMENTS if args.experiment == 'all' else [args.experiment]:
        run(name, args.seed, args.output)


if __name__ == '__main__':
    main()
