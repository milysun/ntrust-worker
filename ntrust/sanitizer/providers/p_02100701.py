import re
import logging

from ..base import BaseSanitizer, BylineInEndOfLine, remove_redundants


log = logging.getLogger('ntrust.sanitizer')


class Sanitizer(BylineInEndOfLine, BaseSanitizer):
    '''
    헤럴드경제 ㅜㅜㅜ
    '''

    RE_REDUNDANTS_HEAD = (
        re.compile('^[\s]*\[.*\][\s]*'),  # mostly it's byline
    )

    def _remove(self, lines=None):
        if lines is None:
            lines = self.content.strip().split('\n')

        lines = remove_redundants(lines, self.RE_REDUNDANTS_HEAD, reverse=False, line_based=False)

        return super(Sanitizer, self)._remove(lines)
