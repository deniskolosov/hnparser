from unittest.mock import patch, Mock

from django.test import TestCase, override_settings

from hackernews_parser.models import Post
from hackernews_parser.tasks import process_request


@patch('hackernews_parser.tasks.requests.get')
class FetchFrontpageTestCase(TestCase):
    def test_process_request(self, requests_patch):
        requests_patch.return_value = Mock(text="""
            <html op="news">
            <head>
                <meta name="referrer" content="origin">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" type="text/css" href="news.css?hMfejlZnJXBFfiQ08F15">
                \n
                <link rel="shortcut icon" href="favicon.ico">
                \n
                <link rel="alternate" type="application/rss+xml" title="RSS" href="rss">
                \n <title>Hacker News</title></head>
            <body>
            <center>
                <table id="hnmain" border="0" cellpadding="0" cellspacing="0" width="85%" bgcolor="#f6f6ef">\n
                    <tr>
                        <td bgcolor="#ff6600">
                            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="padding:2px">
                                <tr>
                                    <td style="width:18px;padding-right:4px"><a href="https://news.ycombinator.com"><img
                                            src="y18.gif" width="18" height="18" style="border:1px white solid;"></a></td>
                                    \n
                                    <td style="line-height:12pt; height:10px;"><span class="pagetop"><b class="hnname"><a
                                            href="news">Hacker News</a></b>\n              <a href="newest">new</a> | <a
                                            href="front">past</a> | <a href="newcomments">comments</a> | <a href="ask">ask</a> | <a
                                            href="show">show</a> | <a href="jobs">jobs</a> | <a href="submit">submit</a>            </span>
                                    </td>
                                    <td style="text-align:right;padding-right:4px;"><span class="pagetop">\n                              <a
                                            href="login?goto=news">login</a>\n                          </span></td>
                                    \n
                                </tr>
                            </table>
                        </td>
                    </tr>
                    \n
                    <tr id="pagespace" title="" style="height:10px"></tr>
                    <tr>
                        <td>
                            <table border="0" cellpadding="0" cellspacing="0" class="itemlist">\n
                                <tr class=\'athing\' id=\'21530860\'>\n
                                    <td align="right" valign="top" class="title"><span class="rank">1.</span></td>
                                    <td valign="top" class="votelinks">
                                        <center><a id=\'up_21530860\' href=\'vote?id=21530860&amp;how=up&amp;goto=news\'>
                                            <div class=\'votearrow\' title=\'upvote\'></div>
                                        </a></center>
                                    </td>
                                    <td class="title"><a href="https://www.facebook.com/100006735798590/posts/2547632585471243/"
                                                         class="storylink">John Carmack: I’m going to work on artificial general
                                        intelligence</a><span class="sitebit comhead"> (<a href="from?site=facebook.com"><span
                                            class="sitestr">facebook.com</span></a>)</span></td>
                                </tr>
                                <tr>
                                    <td colspan="2"></td>
                                    <td class="subtext">\n <span class="score" id="score_21530860">1273 points</span> by <a
                                            href="user?id=jbredeche" class="hnuser">jbredeche</a> <span class="age"><a
                                            href="item?id=21530860">14 hours ago</a></span> <span id="unv_21530860"></span> | <a
                                            href="hide?id=21530860&amp;goto=news">hide</a> | <a href="item?id=21530860">674&nbsp;comments</a>
                                    </td>
                                </tr>
                                \n
                                <tr class="spacer" style="height:5px"></tr>
                                \n
                                <tr class=\'athing\' id=\'21533791\'>\n
                                    <td align="right" valign="top" class="title"><span class="rank">2.</span></td>
                                    <td valign="top" class="votelinks">
                                        <center><a id=\'up_21533791\' href=\'vote?id=21533791&amp;how=up&amp;goto=news\'>
                                            <div class=\'votearrow\' title=\'upvote\'></div>
                                        </a></center>
                                    </td>
                                    <td class="title"><a
                                            href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=c2955f270a84762343000f103e0640d29c7a96f3"
                                            class="storylink">Intel disables Hardware Lock Elision on all current CPUs</a><span
                                            class="sitebit comhead"> (<a href="from?site=kernel.org"><span class="sitestr">kernel.org</span></a>)</span>
                                    </td>
                                </tr>
                                \n
                                <tr class="spacer" style="height:5px"></tr>
                                \n
                                <tr class="morespace" style="height:10px"></tr>
                                <tr>
                                    <td colspan="2"></td>
                                    <td class="title"><a href="news?p=2" class="morelink" rel="next">More</a></td>
                                </tr>
                                \n
                            </table>
                            \n
                        </td>
                    </tr>
                    \n
                    <tr>
                        <td><img src="s.gif" height="10" width="0">
                            <table width="100%" cellspacing="0" cellpadding="1">
                                <tr>
                                    <td bgcolor="#ff6600"></td>
                                </tr>
                            </table>
                            <br>
                            <center><span class="yclinks"><a href="newsguidelines.html">Guidelines</a>\n        | <a
                                    href="newsfaq.html">FAQ</a>\n        | <a href="mailto:hn@ycombinator.com">Support</a>\n        | <a
                                    href="https://github.com/HackerNews/API">API</a>\n        | <a href="security.html">Security</a>\n        | <a
                                    href="lists">Lists</a>\n        | <a href="bookmarklet.html" rel="nofollow">Bookmarklet</a>\n        | <a
                                    href="http://www.ycombinator.com/legal/">Legal</a>\n        | <a
                                    href="http://www.ycombinator.com/apply/">Apply to YC</a>\n        | <a
                                    href="mailto:hn@ycombinator.com">Contact</a></span><br><br>
                                <form method="get" action="//hn.algolia.com/">Search:\n <input type="text" name="q" value=""
                                                                                               size="17" autocorrect="off"
                                                                                               spellcheck="false"
                                                                                               autocapitalize="off"
                                                                                               autocomplete="false"></form>
                                \n
                            </center>
                        </td>
                    </tr>
                    \n
                </table>
            </center>
            </body>
            <script type=\'text/javascript\' src=\'hn.js?hMfejlZnJXBFfiQ08F15\'></script>
            \n
            </html>\n'

        """)
        process_request()
        self.assertEqual(Post.objects.count(), 2)

    def test_process_request_empty_response(self, requests_patch):
        requests_patch.return_value = Mock(text="<html></html")
        process_request()
        self.assertEqual(Post.objects.count(), 0)
