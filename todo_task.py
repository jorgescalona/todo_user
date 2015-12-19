#-*- coding: utf-8 -*-
from openerp import models, fields, api
class TodoTask(models.Model):
	_inherit = 'todo.task'
	# note la ausencia del parametro _name, el mismo no es necesario ya 
	# que hereda este atributo desde el modelo padre
	user_id = fields.Many2one('res.user', 'Responsible')
	date_deadline = fields.Date('Deadline')
""" Se agrega para que borre solo las tareas de un usuario en especifico
	el filtro domain es definido por una lista de condiciones
	donde cada condicion es una tupla, por defecto un operador and se puede usar
	tuberia '|' para agregar la condicion OR """
	@api.multi
	def	do_clear_done(self):
		domain = [('is_done', '=', True), '|', ('user_id', '=',	self.env.uid), ('user_id',	'=',	False)]
		done_recs	=	self.search(domain)
		done_recs.write({'active':	False})
		return True
	@api.one
	def	do_toggle_done(self):
		if self.user_id	!=	self.env.user:
			raise Exception('Solo el responsable de la tarea puede hacer esto!')
		else:
			return super(TodoTask,	self).do_toggle_done()
		
