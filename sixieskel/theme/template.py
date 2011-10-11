import os, copy, subprocess
from zopeskel.vars import StringVar
from zopeskel.base import get_var
from zopeskel.plone3_theme import Plone3Theme


class SixieTheme(Plone3Theme):
    _template_dir = 'templatesj'
    summary = "A Custom Six Feet Up Theme"

    vars = copy.deepcopy(Plone3Theme.vars)
    vars.append(
        StringVar('plone_version',
            'Plone version',
            default='4.1',
           )
    )
    get_var(vars, 'namespace_package').description = 'Namespace package (like plonetheme or Products)'
    get_var(vars, 'namespace_package').description = 'Namespace package (like plonetheme or Products)'
    get_var(vars, 'namespace_package').default = 'Products'
    get_var(vars, 'package').description = 'The package contained namespace package (like policy or theme)'
    get_var(vars, 'package').default = 'theme'
    get_var(vars, 'zope2product').default = False
    get_var(vars, 'description').default = 'An installable theme for Plone 3'
    get_var(vars, 'author').default = 'Six Feet Up, Inc.'
    get_var(vars, 'author_email').default = 'info@sixfeetup.com'
    get_var(vars, 'url').default = 'http://www.sixfeetup.com'
    get_var(vars, 'keywords').default = 'web zope plone theme'
    get_var(vars, 'version').default = '0.1dev'
    get_var(vars, 'skinname').description = 'The skin selection to be added to portal_skins (like SFUP Theme)'
    get_var(vars, 'skinbase').default = 'Plone Basic'
    get_var(vars, 'empty_styles').default = False

    def post(self, command, output_dir, vars):
        if '.svn' in os.listdir(output_dir):
            os.chdir(output_dir)

            subprocess.call('svn ps svn:ignore -F IGNORE.txt .', shell=True)

            os.chdir('../')

        super(SixieTheme, self).post(command, output_dir, vars)
