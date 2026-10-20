"""Reproduce the analytic scientific figures used in S01."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ASSETS = Path(__file__).resolve().parent/'assets'
BG, NAVY, TEAL = '#F5F3EE', '#14233B', '#168A84'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'text.color':NAVY,
                     'axes.labelcolor':NAVY,'xtick.color':NAVY,'ytick.color':NAVY})


def save(fig,name):
    fig.savefig(ASSETS/name,dpi=180,facecolor=BG,bbox_inches='tight')
    plt.close(fig)


def main():
    ASSETS.mkdir(exist_ok=True)
    fig,ax=plt.subplots(figsize=(7,4.4),facecolor=BG)
    ax.set_facecolor(BG)
    ax.axhline(0,color=NAVY,lw=1); ax.axvline(0,color=NAVY,lw=1)
    ax.plot([0,3],[0,4],color=TEAL,lw=3)
    ax.plot([3,3],[0,4],color=NAVY,ls='--',lw=1)
    ax.plot([0,3],[4,4],color=NAVY,ls='--',lw=1)
    ax.scatter([3],[4],color=TEAL,s=80)
    ax.text(3.15,4.05,'3 + 4i',fontsize=18)
    ax.text(0.7,2.4,'r = 5',fontsize=18)
    ax.set(xlim=(-1,5),ylim=(-1,5),xlabel='Real part',ylabel='Imaginary part')
    ax.set_aspect('equal');fig.tight_layout();save(fig,'complex-plane.png')

    phi=np.linspace(0,2*np.pi,401)
    fig,ax=plt.subplots(figsize=(7,4.4),facecolor=BG);ax.set_facecolor(BG)
    ax.axhline(0,color=NAVY,lw=1);ax.axvline(0,color=NAVY,lw=1)
    ax.plot(np.cos(phi),np.sin(phi),color=TEAL,lw=3)
    for angle,label,dx,dy in [(0,'1',0.08,0.05),(np.pi/2,'i',0.06,0.06),(np.pi,'−1',-0.2,0.06),(-np.pi/2,'−i',0.06,-0.12)]:
        x,y=np.cos(angle),np.sin(angle);ax.scatter(x,y,color=NAVY,s=40);ax.text(x+dx,y+dy,label)
    ax.set(xlim=(-1.45,1.45),ylim=(-1.4,1.4),xlabel='Real part',ylabel='Imaginary part')
    ax.set_aspect('equal');fig.tight_layout();save(fig,'unit-circle.png')

    fig,ax=plt.subplots(figsize=(7,4.4),facecolor=BG);ax.set_facecolor(BG)
    ax.plot(phi,(1+np.cos(phi))/2,color=TEAL,lw=3)
    ax.set(xlim=(0,2*np.pi),ylim=(-0.04,1.04),xlabel='Relative phase φ (radians)',ylabel='Plus-basis probability')
    ax.set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],['0','π/2','π','3π/2','2π'])
    ax.grid(alpha=.2);fig.tight_layout();save(fig,'interference.png')


if __name__=='__main__':
    main()
