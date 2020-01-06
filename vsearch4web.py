from flask import Flask, render_template, request,escape
from vsearch import search4letters

app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log','a') as log:
        print(req.form, req.remote_addr,req.user_agent,res,file=log,sep='|')


@app.route('/search4', methods=['GET','POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request,results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data','Remote_addr','User_agent','Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)

@app.route('/game',methods=['POST'])
def view_game() -> 'html':
    contents = []
    with open('game.csv','r') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', '', '', '')
    return render_template('viewlog.html',
                           the_title='View Game',
                           the_row_titles=titles,
                           the_data=contents,)

@app.route('/net',methods=['POST'])
def view_net() -> 'html':
    contents = []
    with open('net_p.csv','r') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', '', '', '')
    return render_template('viewlog.html',
                           the_title='View Net',
                           the_row_titles=titles,
                           the_data=contents,)

@app.route('/01',methods=['GET','POST'])
def entry_01() -> 'html':
    return render_template('01.html',
                           the_title='互联网使用人口')

@app.route('/02',methods=['GET','POST'])
def entry_02() -> 'html':
    return render_template('02.html',
                           the_title='中国手机接入互联网人口与移动游戏用户人口对比')

@app.route('/03',methods=['GET','POST'])
def entry_03() -> 'html':
    return render_template('03.html',
                           the_title='中国游戏产业实际销售收入')

@app.route('/04',methods=['GET','POST'])
def entry_04() -> 'html':
    return render_template('04.html',
                           the_title='游戏用户的男女比例')

@app.route('/05',methods=['GET','POST'])
def entry_05() -> 'html':
    return render_template('05.html',
                           the_title='女性游戏市场实际销售收入占比')

@app.route('/06',methods=['GET','POST'])
def entry_06() -> 'html':
    return render_template('06.html',
                           the_title='中国端游实际销售收入')

@app.route('/zongjie',methods=['GET','POST'])
def entry_zong() -> 'html':
    return render_template('zong.html',
                           the_title='总结')

@app.route('/entry',methods=['GET','POST'])
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='欢迎来到我的世界')

@app.route('/')
@app.route('/start',methods=['GET','POST'])
def start_first() -> 'html':
    return render_template('find.html',
                           the_title='中国互联网游戏发展研究')

if __name__ == '__main__':
    app.run(debug=True)
