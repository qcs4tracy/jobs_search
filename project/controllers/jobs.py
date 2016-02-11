from flask import render_template
from project import app, jobs_db, conf

_db = jobs_db


@app.route('/amz_jobs/<page_num>')
@app.route('/amz_jobs/')
def ListJobs(page_num=None):
    if page_num is None:
        page_num = 1

    page_num = int(page_num)
    count = _db.JobCount()
    nr_per_page = conf.NR_PER_PAGE
    npage = count / nr_per_page
    if npage * nr_per_page < count:
        npage += 1
    records = []
    if page_num > npage:
        return render_template('list.j2', **{'cnt_range': ['-', '-'], 'jobs': records,
                                                           'total_cnt': count, 'show': False})
    p1, p2 = _page_range(page_num, npage)
    _off = (page_num - 1) * nr_per_page
    nr1 = _off + 1
    records = _db.FetchJobs(_off, nr_per_page)

    if len(records) < nr_per_page:
        nr2 = nr1 + len(records) - 1
    else:
        nr2 = nr1 + nr_per_page - 1

    return render_template('list.j2', **{'cnt_range': [nr1, nr2], 'jobs': records,
                                                       'show': True, 'total_cnt': count, 'page_now': page_num,
                                                       'last_page': npage, 'head_page': p1, 'tail_page': p2})


def _page_range(page_num, npage):
    # decide the range of the page_nm
    #  e.g.: [1...5] [6...10] ....
    _pagin = conf.PAGINATION
    r = page_num / _pagin
    if page_num == r * _pagin:  # exactly last page at this range
        r -= 1
    s = r * _pagin + 1
    e = s + _pagin - 1
    if e > npage:
        e = npage

    return s, e
