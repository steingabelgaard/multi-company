from . import models


def post_init_hook(cr, registry):
    """ We should not set the company by default on all existing mail activity types
    when installing this module. Because many standard types need not be
    specialized by company.
    OTOH, when this module is installed it makes sense that new templates
    being created by users have a company set by default. """
    cr.execute("UPDATE mail_activity_type SET company_id=null")
