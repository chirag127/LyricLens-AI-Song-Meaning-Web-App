# Blogger API: Using the API

# bookmark_border
# The Blogger API enables you to integrate Blogger content with your application by using the REST APIs. Before you begin, you will need to set up authorization.

# Introduction
# This document is intended for developers who want to write applications that can interact with the Blogger API. Blogger is a tool for creating websites that allow people to publish their thoughts on an ongoing basis.

# If you're unfamiliar with Blogger concepts, you should read Getting Started before starting to code.

# Authorizing requests and identifying your application
# Every request your application sends to the Blogger APIs needs to identify your application to Google. There are two ways to identify your application: using an OAuth 2.0 token (which also authorizes the request) and/or using the application's API key. Here's how to determine which of those options to use:

# If the request requires authorization (such as a request for an individual's private data), then the application must provide an OAuth 2.0 token with the request. The application may also provide the API key, but it doesn't have to.
# If the request doesn't require authorization (such as a request for public data), then the application must provide either the API key or an OAuth 2.0 token, or both—whatever option is most convenient for you.
# About authorization protocols
# Your application must use OAuth 2.0 to authorize requests. No other authorization protocols are supported. If your application uses Sign In With Google, some aspects of authorization are handled for you.

# Authorizing requests with OAuth 2.0
# Requests to the Blogger APIs for non-public user data must be authorized by an authenticated user.

# This process is facilitated with an OAuth client ID.

# Get an OAuth client ID
# Or create one in the Credentials page.

# The details of the authorization process, or "flow," for OAuth 2.0 vary somewhat depending on what kind of application you're writing. The following general process applies to all application types:

# When your application needs access to user data, it asks Google for a particular scope of access.
# Google displays a consent screen to the user, asking them to authorize your application to request some of their data.
# If the user approves, then Google gives your application a short-lived access token.
# Your application requests user data, attaching the access token to the request.
# If Google determines that your request and the token are valid, it returns the requested data.
# Some flows include additional steps, such as using refresh tokens to acquire new access tokens. For detailed information about flows for various types of applications, see Google's OAuth 2.0 documentation.

# Here's the OAuth 2.0 scope information for the Blogger APIs:


# https://www.googleapis.com/auth/blogger
# To request access using OAuth 2.0, your application needs the scope information, as well as information that Google supplies when you register your application (such as the client ID and the client secret).

# Tip: The Google APIs client libraries can handle some of the authorization process for you. They are available for a variety of programming languages; check the page with libraries and samples for more details.

# Acquiring and using an API key
# Requests to the Blogger APIs for public data must be accompanied by an identifier, which can be an API key or an access token.

# Get a Key
# Or create one in the Credentials page.

# After you have an API key, your application can append the query parameter key=yourAPIKey to all request URLs.

# The API key is safe for embedding in URLs; it doesn't need any encoding.

# Working with blogs
# Retrieving a blog
# You can retrieve information for a particular blog by sending an HTTP GET request to the blog's URI. The URI for a blog has the following format:


# https://www.googleapis.com/blogger/v3/blogs/blogId
# Request

# GET https://www.googleapis.com/blogger/v3/blogs/2399953?key=YOUR-API-KEY
# A user does not need to be authenticated to retrieve a public blog. The application does not need to include Authorization HTTP header for a public blog request; however, you do need to provide the API key.

# Blogger also has private blogs, which require authentication.

# Response
# If the request succeeds, the server responds with an HTTP 200 OK status code and the blog data:


# {
#   "kind": "blogger#blog",
#   "id": "2399953",
#   "name": "Blogger Buzz",
#   "description": "The Official Buzz from Blogger at Google",
#   "published": "2007-04-23T22:17:29.261Z",
#   "updated": "2011-08-02T06:01:15.941Z",
#   "url": "http://buzz.blogger.com/",
#   "selfLink": "https://www.googleapis.com/blogger/v3/blogs/2399953",
#   "posts": {
#     "totalItems": 494,
#     "selfLink": "https://www.googleapis.com/blogger/v3/blogs/2399953/posts"
#   },
#   "pages": {
#     "totalItems": 2,
#     "selfLink": "https://www.googleapis.com/blogger/v3/blogs/2399953/pages"
#   },
#   "locale": {
#     "language": "en",
#     "country": "",
#     "variant": ""
#   }
# }
# Retrieving a blog by its URL
# You can retrieve a blog using its URL by sending an HTTP GET request to the following URI with a url parameter:


# https://www.googleapis.com/blogger/v3/blogs/byurl?url=blog-url
# Request

# https://www.googleapis.com/blogger/v3/blogs/byurl?url=http://code.blogger.com/
# Response
# If the request succeeds, the server responds with an HTTP 200 OK status code and the full representation of the identified blog:


# {
#  "kind": "blogger#blog",
#  "id": "3213900",
#  "name": "Blogger Developers Network",
#  "description": "The official Blogger Developers Network weblog.",
#  "published": "2007-02-09T10:13:10-08:00",
#  "updated": "2012-04-15T19:38:01-07:00",
#  "url": "http://code.blogger.com/",
#  "selfLink": "https://www.googleapis.com/blogger/v3/blogs/3213900",
#  "posts": {
#   "totalItems": 55,
#   "selfLink": "https://www.googleapis.com/blogger/v3/blogs/3213900/posts"
#  },
#  "pages": {
#   "totalItems": 1,
#   "selfLink": "https://www.googleapis.com/blogger/v3/blogs/3213900/pages"
#  },
#  "locale": {
#   "language": "en",
#   "country": "US",
#   "variant": ""
#  }
# }
# Retrieving a user's blogs
# You can retrieve a list of a user's blogs by sending an HTTP GET request to the blogs collection URI:


# https://www.googleapis.com/blogger/v3/users/userId/blogs
# Request

# GET https://www.googleapis.com/blogger/v3/users/self/blogs
# Authorization: /* OAuth 2.0 token here */
# Note: The user must be authenticated to list their own blogs, so you must provide the Authorization HTTP header with the GET request.

# Response
# If the request succeeds, the server responds with an HTTP 200 OK status code and the full representation of the list of the user's blogs:


# {
#   "kind": "blogger#blogList",
#   "items": [
#     {
#       "kind": "blogger#blog",
#       "id": "4967929378133675647",
#       "name": "Brett's Test Blawg",
#       "description": "",
#       "published": "2010-10-06T23:33:31.662Z",
#       "updated": "2011-08-08T06:50:02.005Z",
#       "url": "http://brettmorgan-test-blawg.blogspot.com/",
#       "selfLink": "https://www.googleapis.com/blogger/v3/blogs/4967929378133675647",
#       "posts": {
#         "totalItems": 13,
#         "selfLink": "https://www.googleapis.com/blogger/v3/blogs/4967929378133675647/posts"
#       },
#       "pages": {
#         "totalItems": 1,
#         "selfLink": "https://www.googleapis.com/blogger/v3/blogs/4967929378133675647/pages"
#       },
#       "locale": {
#         "language": "en",
#         "country": "",
#         "variant": ""
#       }
#     }
#   ]
# }

import requests


def create_blog(title, description, url, api_key):
    """Creates a new blog.
    Args:
        title: The title of the blog.
        description: The description of the blog.
        url: The URL of the blog.
        api_key: The API key to use.
    Returns:
        The response from the API.
    """
    url = "https://www.googleapis.com/blogger/v3/blogs"
    data = {"name": title, "description": description, "url": url, "key": api_key}
    response = requests.post(url, data=data)
    return response
