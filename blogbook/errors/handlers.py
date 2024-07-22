from flask import Blueprint, render_template

errors = Blueprint('errors',__name__)

@errors.app_errorhandler(404)
def error_404(error):
    """
    Handle 404 errors by rendering a custom 404 error page.

    This function is triggered whenever a 404 (Not Found) error occurs 
    in the application. It renders the '404.html' template located in the 
    'errors' directory and returns it with a 404 status code.

    Parameters:
    error: The error object passed by the Flask error handler.

    Returns:
    A tuple containing the rendered template for the 404 error page 
    and the HTTP status code 404.
    """
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(403)
def error_403(error):
    """
    Handles 403 Forbidden errors and returns the appropriate error page.

    Args:
        error: The error object containing details of the 403 error.

    Returns:
        A tuple containing the rendered 403 error template and the error code 403.
    """
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_500(error):
    """
    Handle 500 Internal Server Error.

    This function is registered as an error handler for 500 Internal Server Errors.
    It renders the '500.html' template from the 'errors' directory and returns it 
    with a 500 HTTP status code.

    Args:
        error (Exception): The error that triggered the 500 error handler.

    Returns:
        tuple: A tuple containing the rendered '500.html' template and the 500 status code.
    """
    return render_template('errors/500.html'), 500