from flask import Flask, render_template, request, escape
from flask_bootstrap import Bootstrap
from bokeh.resources import CDN
import getdata


app=Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():

    l = {"^IXIC":"NASDAQ","^NYA":"NYSE","^XAX":"AMEX"}
    r = []

    for k,v in l.items():
        r1 = getdata.get(k,v) 
        r.append(r1)

    cdn_js=CDN.js_files[0]
    cdn_css=CDN.css_files[0]

    return render_template("index.html",r=r,cdn_css=cdn_css,cdn_js=cdn_js)



@app.route('/plot/<n>')
def plot(n):

    # if n == "Google":
    #     a = "GOOG"

    # elif n == "Facebook":
    #     a = "FB"
    # else:
    #      a = "DXC"

    l = {"Google":"GOOG","Facebook":"FB","DXC":"DXC","Tesla":"TSLA","Apple":"AAPL","IBM":"IBM",
            "Twitter":"TWTR","Amazon":"AMZN","Microsoft":"MSFT","Dell":"DELL","Cisco":"CSCO","VmWare":"VMW",
            "AMD":"AMD","Intel":"INTC","Dow Jones":"^DJI","NASDAQ":"^IXIC","NYSE":"^NYA","AMEX":"^XAX","Alibaba":"BABA"}

    a = l[n]

    cdn_js=CDN.js_files[0]
    cdn_css=CDN.css_files[0]


    r1 = getdata.get(a,n) 

    return render_template("plot.html",script1=r1[0],div1=r1[1],cdn_css=cdn_css,cdn_js=cdn_js,n1=r1[2],n=n)


@app.route('/search/',methods=['GET'])
def search():

    sname = escape(request.args.get("sname"))

    ln = len(sname)

    if ln > 10 or ln == 0:
        return render_template("error.html", n="Error in search, stock mark is longer than 10 or 0")

    r1 = getdata.getsearch(sname)


    if r1 != None:
        print("NONE")
        
        cdn_js=CDN.js_files[0]
        cdn_css=CDN.css_files[0]
        return render_template("search.html",script1=r1[0],div1=r1[1],cdn_css=cdn_css,cdn_js=cdn_js,n=sname)

    else:
        return render_template("error.html", n="Error in search, wrong stock mark or somethin else get wrong")



if __name__ == "__main__":
    app.run(debug=True)