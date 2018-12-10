# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
	_inherit = 'res.partner'
	ref = fields.Char(string='Referencia interna')

	@api.model
	def create(self, vals):
		cr = self.env.cr
		sql = "select ref from res_partner where ref != ''"
		cr.execute(sql)
		tabla = cr.fetchall()
		maxc=5000
		maxp=0
		for t in tabla:
			try:
				if int(t[0])>5000:
					if int(t[0])>maxc:
						maxc=int(t[0])
			except ValueError:
				print("")
			try:
				if int(t[0])<5000:
					if int(t[0])>maxp:
						maxp=int(t[0])
			except ValueError:
				print("")


		if vals.get('supplier') == False:
			vals['ref'] = maxp+1
			
		else:
			vals['ref'] = maxc+1

		return super(ResPartner, self).create(vals)

class ProducProduct(models.Model):
	_inherit = 'product.product'	 
	_sql_constraints = [(
		'default_code_unique',
		'unique(default_code)',
		'la referencia interna del producto ya existe, favor de modificarla'
		)]
	
class ProTemplate(models.Model):
	_inherit = 'product.template'	 
	default_code = fields.Char(string='Referencia interna',requiered=True)

	