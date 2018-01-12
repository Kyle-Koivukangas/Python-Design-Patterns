# MVC is a UI pattern, intended to separate internal representations of data from the ways it is presented to/accepted from the user.

# this exmaple uses flask (@app.route is a flask decorator)

@app.route('/')
def example_page():
    """ Searches the database for entries, then displays them. """
    db = get_db()
    query =db.execute('select * from entries order by id desc')
    entries= query.fetchall()
    return render_template('example_page.html', entries=entries)

# the decorator will map the route to the controller for example_page()
# then in the controler it will connect to the db and get the specified data from the db
# then it will pass the data to the where it will be rendered according to the template (uses Jinja for templates)

# the template abstracts how the data is displayed from the data itself,
# the same data could be passed to multiple templates and be displayed multiple ways

#example jinja template:
"""

{% for entry in entries %}
    <li>
        <h2>{{ entryy,title }}</h2>
        <div>{{ entry.text }}</div>
    </li>
{% else %}
    <li><em>No entries yet.</em></li>
{% endfor %}

"""
