from odoo import api, fields, models


class CreateOrderWizard(models.Model):
    _name = "create.order.wizard"
    _description = "Create Order Wizard"

    partner_id = fields.Many2one('res.partner','Vendor')
    order_line = fields.One2many('order.line', 'create_order_id', string='Order Lines')

    def action_confirmed(self):
        return

    @api.model
    def create(self,vals):
        created_record= self.env['purchase.order'].create(vals)
        return created_record



