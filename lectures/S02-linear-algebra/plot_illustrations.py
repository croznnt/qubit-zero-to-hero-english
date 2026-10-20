"""Reproduce the numerical illustrations added to S02."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent/'assets'
BG, NAVY, TEAL, ORANGE = '#F5F3EE', '#14233B', '#168A84', '#BD6632'
plt.rcParams.update({'font.size':17,'font.family':'DejaVu Sans','text.color':NAVY,
                     'axes.labelcolor':NAVY,'xtick.color':NAVY,'ytick.color':NAVY})


def canvas():
    f,a=plt.subplots(figsize=(8,5),facecolor=BG)
    a.set_facecolor(BG)
    return f,a


def save(f,name):
    f.tight_layout()
    f.savefig(ROOT/name,dpi=180,bbox_inches='tight',facecolor=BG)
    plt.close(f)


def vector(a,x,y,color,label):
    a.quiver(0,0,x,y,angles='xy',scale_units='xy',scale=1,color=color,width=.012)
    a.text(x+.06,y+.06,label,color=color,fontsize=17)


def main():
    ROOT.mkdir(exist_ok=True)
    f,a=canvas()
    x=np.arange(2)
    a.bar(x-.18,[1,1],width=.36,color=NAVY,label='Before normalization')
    a.bar(x+.18,[1/np.sqrt(2)]*2,width=.36,color=TEAL,label='After normalization')
    a.set_xticks(x,['Component 1','Component 2'])
    a.set(ylabel='Component magnitude',ylim=(0,1.4))
    a.legend(loc='upper center',fontsize=14)
    save(f,'normalization.png')

    f,a=canvas()
    a.plot([-0.2,2.5],[-0.2,2.5],color=NAVY,alpha=.35,label='Projector range')
    vector(a,2,1,NAVY,'w = (2, 1)')
    vector(a,1.5,1.5,TEAL,'Pw = (1.5, 1.5)')
    a.plot([2,1.5],[1,1.5],ls='--',color=ORANGE,lw=2,label='Removed component')
    a.set(xlim=(-.2,2.7),ylim=(-.2,2.6),xlabel='Real coordinate 1',ylabel='Real coordinate 2')
    a.set_aspect('equal');a.legend(loc='upper left',fontsize=12)
    save(f,'projection.png')

    f,a=canvas()
    t=np.linspace(0,2*np.pi,401)
    a.plot(np.cos(t),np.sin(t),color=NAVY,alpha=.35)
    vector(a,1,0,NAVY,'v')
    vector(a,1/np.sqrt(2),1/np.sqrt(2),TEAL,'Rv')
    a.set(xlim=(-1.25,1.5),ylim=(-1.25,1.4),xlabel='Real coordinate 1',ylabel='Real coordinate 2')
    a.set_aspect('equal');a.grid(alpha=.15)
    save(f,'unitarity.png')

    f,a=canvas()
    plus=np.array([1,1])/np.sqrt(2)
    minus=np.array([1,-1])/np.sqrt(2)
    vector(a,*plus,TEAL,'q+ stays fixed')
    vector(a,*minus,NAVY,'q−')
    vector(a,*(-minus),ORANGE,'Xq− = −q−')
    a.axhline(0,color=NAVY,lw=.6);a.axvline(0,color=NAVY,lw=.6)
    a.set(xlim=(-1.25,1.5),ylim=(-1.25,1.3),xlabel='Real coordinate 1',ylabel='Real coordinate 2')
    a.set_aspect('equal');save(f,'eigenvectors.png')

    f,axes=plt.subplots(1,2,figsize=(8,4),facecolor=BG)
    for ax,data,title in zip(axes,[np.eye(2),np.ones((2,2))],['Matrix exponential','Elementwise exponential']):
        ax.imshow(data,cmap='Blues',vmin=0,vmax=1)
        for i in range(2):
            for j in range(2):ax.text(j,i,str(int(data[i,j])),ha='center',va='center',fontsize=30,color='white' if data[i,j] else NAVY)
        ax.set_title(title,fontsize=16);ax.set_xticks([]);ax.set_yticks([])
    save(f,'exponential.png')

    f,a=canvas()
    t=np.linspace(0,2*np.pi,401)
    a.plot(t,np.cos(t/2)**2,color=NAVY,lw=3,label='Outcome 0')
    a.plot(t,np.sin(t/2)**2,color=TEAL,lw=3,label='Outcome 1')
    a.set(xlim=(0,2*np.pi),ylim=(-.03,1.06),xlabel='Rotation angle θ (radians)',ylabel='Probability')
    a.set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],['0','π/2','π','3π/2','2π'])
    a.legend(loc='upper center',fontsize=14);a.grid(alpha=.15)
    save(f,'rotation.png')


if __name__=='__main__':
    main()
