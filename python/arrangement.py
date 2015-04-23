#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Author: wg_koro
    License: MIT License

    This script arrange photos in Dropbox/Camera Uploads

    Requirement:
    - Python 2.5 < 3.x

    How to use -> Please see README
"""
import os
import sys
import re
import shutil
import traceback
from optparse import OptionParser

VERSION = '1.1'

class Arrangement:
    def __init__(self):
        self.pattern_str = '^2[0-9]+.+\.(jpg|png|mov)'
        self.testmode = False
        self.create_date_flg = True
        self.camera_root = os.path.realpath(os.path.dirname(__file__))
        self._files = []
        self._dirs = []


    def parse_command(self):
        """
        Parse command line.
        Set flag of 'test mode', and flag of 'no creation date directory'
        """
        usage = u'%prog [Options]\nDetailed options... -h or --help'
        parser = OptionParser(usage=usage, version=VERSION)

        parser.add_option(
            '--test',
            action = 'store_true',
            dest = 'test_flg',
            help = 'Run with test mode (it won\'t delete original photos)',
        )
        parser.add_option(
            '--nodate',
            action = 'store_false',
            dest = 'create_date_flg',
            help = 'Do not create date directory',
        )
        parser.set_defaults(
            test_flg = False,
            create_date_flg = True,
        )

        options, args = parser.parse_args()
        if options.test_flg:
            self.testmode = True

        if not options.create_date_flg:
            self.create_date_flg = False

        self._start_arrangement()


    def _start_arrangement(self):
        """
        Start process.
        """
        testmode_str = ''
        if self.testmode:
            testmode_str = '[ TEST MODE ]'

        print '=====%s Arrangement START! =====' % testmode_str

        self._pattern = re.compile(self.pattern_str)
        self._get_root_list()
        if self._files and not self.testmode:
            self._delete_root_files()

        print '-----%s Arrangement END! -----' % testmode_str


    def get_date_info(self, file_name):
        """
        Get 'year', 'month', 'day' from file name.
        """
        error = 'File pattern is not valid."%s" is skipped.'
        tmp = file_name.split(' ')
        if len(tmp) > 3:
            print error % file_name
            return {}

        dates = tmp[0].split('-')
        if len(dates) != 3:
            print error % file_name
            return {}

        month = dates[1]
        if int(month) < 10:
            month = month[1:]

        day = dates[2]
        if int(day) < 10:
            day = day[1:]

        return {
            'year'  : dates[0],
            'month' : month,
            'date'  : day,
        }


    def _get_root_list(self):
        """
        Get files in 'Camera Uploads' directory.
        If file name matchs file pattern,copy it.
        """
        root_files = os.listdir(self.camera_root)
        if not root_files:
            print 'File not found!'
            return

        for f in root_files:
            path = os.path.join(self.camera_root, f)
            if self._pattern.match(f):
                destination = self._get_destination(f)
                if not destination:
                    continue

                if not self._copy_file(path, destination):
                    continue

                self._files.append(path)

            if os.path.isdir(path):
                self._dirs.append(path)

        if not self._files:
            print 'No photos to move.'


    def _get_destination(self, file_name):
        """
        Get destination path for copying.
        """
        move_to = ''

        date_info = self.get_date_info(file_name)
        if not date_info:
            return move_to

        year = os.path.join(self.camera_root, date_info['year'])
        month = os.path.join(year, date_info['month'])
        date = os.path.join(month, date_info['date'])

        try:
            self._make_dir(year)
            self._make_dir(month)
            if self.create_date_flg:
                self._make_dir(date)
                move_to = os.path.join(date, file_name)
            else:
                move_to = os.path.join(month, file_name)
        
        except:
            print 'Making directory failed! file[ %s ] error[ %s ]\n' % (file_name, traceback.format_exc())

        return move_to


    def _make_dir(self, target_dir):
        if not target_dir in self._dirs:
            if not os.path.exists(target_dir):
                os.mkdir(target_dir, 0775)

            self._dirs.append(target_dir)


    def _copy_file(self, org_path, destination):
        """
        Copy photo to new path.
        If new path(file) already exists, skip it.
        """
        if os.path.exists(destination):
            print 'Destination "%s" already exists.Skipped!\n' % destination
            return True

        try:
            print 'Copying "%s" to "%s".' % (org_path, destination)
            shutil.copyfile(org_path, destination)
            print '...ok.\n'
            return True
        except:
            print 'Copy error! original_file[ %s ] destination[ %s ] error[ %s ]\n' % (org_path, destination, traceback.format_exc())
            return False


    def _delete_root_files(self):
        """
        Delete photos in root directory.
        """
        if not self._files:
            print 'Photo for deletion not found.'
        else:
            for f in self._files:
                try:
                    print 'Deleting original file ("%s")' % f
                    os.remove(f)
                    print '...ok.\n'
                except:
                    print 'Delete file failed! file[ %s ] error[ %s ]\n' % (f, traceback.format_exc())





if __name__ == '__main__':
    a = Arrangement()
    # Override regular expression for finding photos
    #a.pattern_str = '^.+'
    a.parse_command()
