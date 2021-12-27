#from django.shortcuts import render

#def index(request):
#    return render(request,"app/index.html")

from django.shortcuts import render
from .forms import CalcPlusForm

import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot

def index(request):
    fig = go.Figure(go.Scatter(x=[], y=[]), layout=go.Layout(width=400, height=400))
    params = { #辞書
        'title':'2点を通る直線',
        "ans":"",
        'forms': CalcPlusForm(),
        "graph":fig.to_html(fig,include_plotlyjs=False)
    }
    if (request.method == 'POST'):
        #(a,b),(c,d)
        a=float(request.POST['val1'])
        b=float(request.POST['val2'])
        c=float(request.POST['val3'])
        d=float(request.POST['val4'])
        

        midx=(a+c)/2
        midy=(b+d)/2

        if(abs(a-c)>=abs(b-d)):
            H=1.5*(abs(a-c)/2)
        else:
            H=1.5*(abs(b-d)/2)
               
        A=d-b
        B=-c+a
        C=d*(c-a)-c*(d-b)

        if(B==0):
            px1=-C/A
            py1=100000
            px2=-C/A
            py2=-100000
        else:
            px1=100000
            py1=-(A/B)*px1-(C/B)
            px2=-100000
            py2=-(A/B)*px2-(C/B)

        params['forms'] = CalcPlusForm(request.POST)#保持しているように見せる
        params['ansa'] = A
        params['ansb'] = B
        params['ansc'] = C

        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[a,c], y=[b,d] , 
                                   mode="lines + markers+text",
                                   text=["点1","点2"],
                                   name="segment",
                                   textposition="top center",
                                   marker={"opacity":0.8,"color":px.colors.qualitative.Plotly,"size":10},
                                   line={"color":"black"}))

        fig.add_trace(go.Scatter(x=[px1,px2], y=[py1,py2] , 
                                   mode="lines",
                                   name="line",
                                   line={"color":"black","dash":"dot"}))
        fig.update_layout(width=400,height=400,
                          xaxis=dict(title="x",range=(midx-H,midx+H)),
                          yaxis=dict(title="y",range=(midy-H,midy+H),anchor="x"),
                          dragmode="pan")

#        fig.show(config=dict({'scrollZoom': True}))

#        params["graph"]=fig.to_html(fig,include_plotlyjs=False)

        params["graph"]=plot(fig, output_type='div', include_plotlyjs=False,config=dict({'scrollZoom': True,
                                                                                         'displaylogo': False,
                                                                                         'editable': True,
                                                                                         'modeBarButtonsToRemove':["zoom2d","select2d","lasso2d","toggleSpikelines","autoScale2d","hoverCompareCartesian"]}))

    return render(request, 'app/index.html', params)