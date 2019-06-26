
from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.models.annotations import Title

start=datetime.datetime(2018,11,1)
end=datetime.datetime(2019,5,10)

d = data.DataReader(name="GOOG",data_source="yahoo",start=start,end=end)

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

p = figure(x_axis_type='datetime', width=1000, height=300,sizing_mode="scale_width")
t = Title()
t.text = "Candlestick Chart"
p.title= t
p.grid.grid_line_alpha = 0.3

hours_12 = 12*60*60*1000

p.segment(d.index,d.High,d.index,d.Low,color="black")

p.rect(d.index[d.Status=="Increase"],d.Middle[d.Status=="Increase"],
    hours_12,d.Height[d.Status=="Increase"],fill_color='#CCFFFF',line_color="black")

p.rect(d.index[d.Status=="Decrease"],d.Middle[d.Status=="Decrease"],
    hours_12,d.Height[d.Status=="Decrease"],fill_color='#FF3333',line_color="black")


output_file("a_plot_2.html")

show(p)
