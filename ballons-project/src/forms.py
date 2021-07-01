from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, DecimalField, IntegerField, RadioField
from wtforms.validators import Required	



class TransaccionForm(Form):
	peso = DecimalField('Peso', [validators.Length(min=4, max=25)])
	tipo_peso = RadioField('Tipo de Peso',  choices=['Peso Limpio', 'Peso Sucio', 'Scrap'])
	id_producto = IntegerField('ID Producto', [validators.Length(min=6, max=35)])
	id_balanza = IntegerField('ID Balanza', [validators.Length(min=6, max=35)])
	id_transaccion = IntegerField('ID Transaccion', [validators.Length(min=6, max=35)])
	tipo_transaccion = RadioField('Tipo de Transaccion', choices=['Produccion', 'Impresion'])
	id_usuario = IntegerField('ID Usuario', [validators.Length(min=4, max=25)])
	accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

#Example
class RegistrationForm(Form):
	username = StringField('Username', [validators.Length(min=4, max=25)])
	email = StringField('Email Address', [validators.Length(min=6, max=35)])
	password = PasswordField('New Password', [
		validators.DataRequired(),
		validators.EqualTo('confirm', message='Passwords must match')
	])
	confirm = PasswordField('Repeat Password')
	accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])