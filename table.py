from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('table', __name__, url_prefix='/')


@bp.route('/table', methods=('GET', 'POST'))
def table():

