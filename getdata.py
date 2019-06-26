
from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.models.annotations import Title
from bokeh.embed import components
from bokeh.resources import CDN

def get(n,b):

    r = []
    
    now = datetime.datetime.now()
    t = str(now.strftime("%Y,%m,%d"))

    y = int(t[0:4])
    m = int(t[6])
    d = int(t[8:10]) 

    start=datetime.datetime(2019,1,1)
    end=datetime.datetime(y,m,d)

    d = data.DataReader(name=n,data_source="yahoo",start=start,end=end)

    def inc_dec(c,o):
        if c > o:
            value = "Increase"
        elif c < o:
            value = "Decrease"
        else:
            value = "Equal"

        return value

    d["Status"] = [inc_dec(c,o) for c,o in zip(d.Close,d.Open)]
    d["Middle"] = (d.Open + d.Close)/2
    d["Height"] = abs(d.Close-d.Open)

    p = figure(x_axis_type='datetime', width=1000, height=245,sizing_mode="scale_width")
    p.yaxis.axis_label = 'usd'
    
    t = Title()

    p.title= t
    p.grid.grid_line_alpha = 0.3

    hours_12 = 12*60*60*1000

    p.segment(d.index,d.High,d.index,d.Low,color="black")




    p.rect(d.index[d.Status=="Increase"],d.Middle[d.Status=="Increase"],
        hours_12,d.Height[d.Status=="Increase"],fill_color='#CCFFFF',line_color="black")


    p.rect(d.index[d.Status=="Decrease"],d.Middle[d.Status=="Decrease"],
        hours_12,d.Height[d.Status=="Decrease"],fill_color='#FF3333',line_color="black")


    script, div = components(p)

    cdn_js=CDN.js_files[0]
    cdn_css=CDN.css_files[0]

    re = [script,div,n,b,cdn_js,cdn_css]

    return re


def getsearch(n):

    r = []
    
    now = datetime.datetime.now()
    t = str(now.strftime("%Y,%m,%d"))

    y = int(t[0:4])
    m = int(t[6])
    d = int(t[8:10]) 

    start=datetime.datetime(2019,1,1)
    end=datetime.datetime(y,m,d)

    try:

        d = data.DataReader(name=n,data_source="yahoo",start=start,end=end)

        def inc_dec(c,o):
            if c > o:
                value = "Increase"
            elif c < o:
                value = "Decrease"
            else:
                value = "Equal"

            return value

        d["Status"] = [inc_dec(c,o) for c,o in zip(d.Close,d.Open)]
        d["Middle"] = (d.Open + d.Close)/2
        d["Height"] = abs(d.Close-d.Open)

        p = figure(x_axis_type='datetime', width=1000, height=245,sizing_mode="scale_width")

        p.yaxis.axis_label = 'usd'

        t = Title()

        p.title= t
        p.grid.grid_line_alpha = 0.3

        hours_12 = 12*60*60*1000

        p.segment(d.index,d.High,d.index,d.Low,color="black")


        p.rect(d.index[d.Status=="Increase"],d.Middle[d.Status=="Increase"],
            hours_12,d.Height[d.Status=="Increase"],fill_color='#CCFFFF',line_color="black")


        p.rect(d.index[d.Status=="Decrease"],d.Middle[d.Status=="Decrease"],
            hours_12,d.Height[d.Status=="Decrease"],fill_color='#FF3333',line_color="black")


        script, div = components(p)

        cdn_js=CDN.js_files[0]
        cdn_css=CDN.css_files[0]

        re = [script,div,n,cdn_js,cdn_css]

        return re

    except:
        print("Error, wrong stock mark")


