import os
os.environ['MPLCONFIGDIR']='/tmp/mpl_gsf'
import geopandas as gpd,pandas as pd,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge,Circle,Patch
from matplotlib import patheffects as pe
from pathlib import Path
P=Path(__file__).resolve().parents[1]
df=pd.read_csv(P/'data/GSF_Geography_Country_ResearchIntensity_v1.csv')
world=gpd.read_file(str(P/'basemap/naturalearth_lowres.shp'))
plt.rcParams.update({'font.family':'DejaVu Sans','pdf.fonttype':42,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(22,12),facecolor='white');ax.set_facecolor('#e8f3f7')
world.plot(ax=ax,color='#eee9db',edgecolor='#9aacae',linewidth=.43,zorder=1)
counts=dict(zip(df.Country,df.Records)); counts['United States of America']=counts['United States']
world['N']=world.name.map(counts)
world.dropna(subset=['N']).plot(ax=ax,column='N',cmap='YlGnBu',vmin=0,vmax=222,edgecolor='#7b9494',linewidth=.5,zorder=2,alpha=.75)
# a cartographic background is used; no unverified global aquifer boundaries are drawn
loc={'India':(79,22),'China':(104,37),'United States':(-100,38),'Pakistan':(68,31),'Bangladesh':(91,24),'Mexico':(-103,24),'Italy':(13,42),'Iran':(54,32),'Argentina':(-64,-36),'Canada':(-110,57),'Ghana':(-2,8),'Saudi Arabia':(44,24),'Ethiopia':(39,9),'Greece':(23,39),'Brazil':(-53,-13)}
# explicitly controlled label locations to keep country values visible
lab={'India':(102,3),'China':(129,54),'United States':(-135,20),'Pakistan':(48,58),'Bangladesh':(125,18),'Mexico':(-125,2),'Italy':(-9,68),'Iran':(42,8),'Argentina':(-91,-47),'Canada':(-141,73),'Ghana':(-23,-15),'Saudi Arabia':(23,-22),'Ethiopia':(45,-43),'Greece':(-1,49),'Brazil':(-29,-33)}
C=['#cc5149','#3279bd','#8660b1','#4aa178'];keys=['As','F','U','Cr']
for country,(lon,lat) in loc.items():
    r=df[df.Country==country].iloc[0]; vals=np.array([int(r[k]) for k in keys]);total=vals.sum();radius=2.0+4.1*np.sqrt(r.Records/222)
    a=90
    for v,c in zip(vals,C):
        if v:
            b=360*v/total;ax.add_patch(Wedge((lon,lat),radius,a,a+b,facecolor=c,edgecolor='white',lw=.45,zorder=8));a+=b
    ax.add_patch(Circle((lon,lat),radius,facecolor='none',edgecolor='#1a3746',lw=1,zorder=9))
    x,y=lab[country]
    txt=f'{country}  N={int(r.Records)}\nAs {int(r.As)}  ·  F {int(r.F)}  ·  U {int(r.U)}  ·  Cr {int(r.Cr)}'
    ax.annotate(txt,xy=(lon,lat),xytext=(x,y),textcoords='data',ha='center',va='center',fontsize=8.1,fontweight='medium',color='#173746',zorder=15,
       bbox=dict(boxstyle='round,pad=.32',fc='white',ec='#b5c9cc',alpha=.96,lw=.65),
       arrowprops=dict(arrowstyle='-',color='#637c85',lw=.65,shrinkA=4,shrinkB=4,connectionstyle='arc3,rad=.08'))
ax.set_xlim(-178,179);ax.set_ylim(-62,84);ax.axis('off')
fig.suptitle('GLOBAL AQUIFER CONTEXT AND GEOTOXICITY RESEARCH EVIDENCE',fontsize=19,fontweight='bold',color='#143848',y=.971)
fig.text(.5,.935,'Country-level research intensity and contaminant-specific literature representation • frozen 892-record analytical subset',ha='center',fontsize=11,color='#385a65')
leg=[Patch(facecolor=c,label=k) for c,k in zip(C,['Arsenic (As)','Fluoride (F)','Uranium (U)','Chromium (Cr)'])]
fig.legend(handles=leg,ncol=4,loc='lower center',bbox_to_anchor=(.5,.092),frameon=False,fontsize=10)
fig.text(.5,.072,'Pie sectors = contaminant-specific publication representations (non-mutually-exclusive); N = country research-record count.',ha='center',fontsize=9.2)
fig.text(.5,.051,'Base map shows countries, NOT verified aquifer-system boundaries. Shading and symbols indicate research intensity, NOT contamination severity.',ha='center',fontsize=9.3,fontweight='bold',color='#923d31')
fig.text(.5,.031,'Data: GSF frozen country evidence table (756 country-counting eligible records). Geography: Natural Earth. Vector-drawn with Python/Matplotlib.',ha='center',fontsize=8.4,color='#54636c')
fig.subplots_adjust(top=.90,bottom=.13,left=.018,right=.982)
for ext in ['png','pdf','svg']:
    f=P/'figures'/f'GSF_Integrated_Global_Evidence_Code_600dpi.{ext}'
    fig.savefig(f,dpi=600,facecolor='white')
    print(f, f.stat().st_size)
plt.close(fig)
from PIL import Image
im = Image.open(P / 'figures' / 'GSF_Integrated_Global_Evidence_Code_600dpi.png')
print('Dimensions:', im.size, 'DPI:', im.info.get('dpi'))
