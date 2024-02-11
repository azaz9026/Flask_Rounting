# Significance of URL redirection
'''
1) Reorganization: If you reorganize your website's structure or change the URL of a page, redirection helps maintain backward compatibility for the users who might have bookmarked or accessed the old url.
2) Content Migration: If you change the content of a page, redirection helps maintain backward compatibility for the users who might have bookmarked or accessed the old url.
3) SEO: If you change the URL of a page, redirection helps improve the search engine ranking of the page.
4) Security: If you change the URL of a page, redirection helps maintain the security of the website.
5) Accessibility: If you change the URL of a page, redirection helps maintain the accessibility of the website.
6) User Friendly: If you change the URL of a page, redirection helps make the website user-friendly.
'''

from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
@app.route('/')
def home():
    return "<p>Home Page </p>"

# Define a route for "/page-1"
@app.route('/page-1')
def page_1():
    # Redirect to "/page-2" with a 302 status code (temporary redirect)
    return redirect(url_for('page_2'), 302)  # 302 status code means temporary redirect

# Define a route for "/page-2"
@app.route('/page-2')
def page_2():
    # Render the "page-2.html" template
    return render_template("page-2.html")

# Define a route for "/about"
@app.route('/about')
def about():
    return "<p>About Page </p>"

# Define a route for "/contact"
@app.route('/contact')
def contact():
    return "<p>Contact Page </p>"

# Run the app
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)