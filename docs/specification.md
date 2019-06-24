# Datarobot home test Julia Tkachova
# Overview
Github OAuth application which replicates own code to users repository
#Libraries used:
- Flask
- GitHub-Flask is an extension to Flask that allows you authenticate your users via - GitHub using OAuth protocol and call GitHub API methods.
- GitPython for git related operations(push and pull repository)
- SqlAlchemy for database handling(storing user tokens)
- alembic- for easy database migration management in case of future database extension
- unittest - for application unit testing

# Application workflow:
If the user calls main page index.html will be shown with button get started which will redirect to /login endpoint.

Login endpoint requires GitHub authentification.

It will redirect the user to GitHub. If the user accepts the authorization request GitHub will redirect the user to callback URL(**/github-callback**) with the OAuth code parameter. Then the extension will make another request to GitHub to obtain an access token, the application will request specific scope: access to public repositories and general user info(users profile data, excluding email and followings)

If request if succeded, the application will be redirected to **/repo** endpoint, which will check if repository exists in user's profile, if not the application will create a mirror of its own application code. If operation success, the user will be redirected to the index page with a link to the newly created repository.  If **/repo** endpoint will be called directly without authentification, the user will be redirected to the index page with a suggestion to login.

Application contains logout feature, however it accessible only by endpoint /logout and doesn't refer to any UI element on the index page.

# ToDo
- For production load please consider taking database with stored auth tokens outside the docker container or get rid of the database due to one-time operation, so it might be not required to store user session

- For production workload, proper SSL and domain should be used for security reasons.

- extend unit tests with more real examples.
