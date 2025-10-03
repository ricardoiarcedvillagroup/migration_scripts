from odoo.upgrade import util
import logging

_logger = logging.getLogger(__name__)

XID = "dsd_maintenance.maintenance_request_activity_report_view_graph"


def migrate(cr, version):
    """
    Desengancha las acciones y elimina vista.
    """
    with util.skippable_cm():
        vid = util.ref(cr, XID)
        if not vid:
            _logger.info("Vista %s no encontrada, nada que remover.", XID)
            return

        cr.execute("UPDATE ir_act_window SET view_id = NULL WHERE view_id = %s", (vid,))
        cr.execute("DELETE FROM ir_act_window_view WHERE view_id = %s", (vid,))

        util.remove_view(cr, xml_id=XID, silent=True)
        _logger.info("Vista removida %s para la migración.", XID)
