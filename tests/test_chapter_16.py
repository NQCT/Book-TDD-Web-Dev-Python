#!/usr/bin/env python3
import unittest

from book_tester import ChapterTest

class Chapter16Test(ChapterTest):
    chapter_no = 16

    def test_listings_and_commands_and_output(self):
        self.parse_listings()
        self.sourcetree.start_with_checkout(self.chapter_no)
        self.prep_virtualenv()

        # sanity checks
        self.assertEqual(self.listings[0].type, 'output')
        self.assertEqual(self.listings[1].type, 'output')
        self.assertEqual(self.listings[2].type, 'code listing')

        # skips
        #self.skip_with_check(22, 'switch back to master') # comment

        self.sourcetree.run_command('rm accounts/tests.py')

        # hack fast-forward
        skip = False
        if skip:
            self.pos = 65
            self.sourcetree.run_command('git checkout {0}'.format(
                self.sourcetree.get_commit_spec('ch15l035')
            ))

        while self.pos < len(self.listings):
            print(self.pos)
            self.recognise_listing_and_process_it()

        self.assert_all_listings_checked(self.listings)

        # tidy up any .origs from patches
        self.sourcetree.run_command('find . -name \*.orig -exec rm {} \;')
        self.check_final_diff(self.chapter_no)


if __name__ == '__main__':
    unittest.main()
