from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, ValidationError, EqualTo, IPAddress, Required
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import User, DeviceType


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    #openid = StringField('openid',validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password', validators=[
                                    DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('user is exists,input other username.')


class SingleForm(FlaskForm):
    ipaddress = StringField('IP address',
                            validators=[DataRequired(), IPAddress()])
    device_model = SelectField(label=u'设备型号', 
                               default=u'请选择设备型号',
                               validators=[Required(u'请选择设备型号')], 
                               coerce=str,
                               )
    login_type = SelectField(label=u'登陆方式',
                             default=[u'请选择登陆方式'],
                             choices=[('telnet', 'Telnet'), ('ssh', 'SSH')],
                             validators=[Required(u'请选择登陆方式')],
                             coerce=str,
                             )
    username = StringField('Username')
    password = PasswordField('Password')
    enable_password = PasswordField(
        'Enalbe Password', validators=[DataRequired()])
    submit = SubmitField(u'普通巡检')
    submit2 = SubmitField(u'深度巡检')

    def __init__(self, *args, **kwargs):
        super(SingleForm, self).__init__(*args, **kwargs)
        self.device_model.choices = [(device.device_model, device.device_model)
                                     for device in DeviceType.query.order_by(DeviceType.id).all()]
                                     

class ConfigForm(FlaskForm):
    ipaddress = StringField('IP address',
                            validators=[DataRequired(), IPAddress()])
    device_model = SelectField(label=u'设备型号', 
                               default=u'请选择设备型号',
                               validators=[Required(u'请选择设备型号')], 
                               coerce=str,
                               )
    login_type = SelectField(label=u'登陆方式',
                             default=[u'请选择登陆方式'],
                             choices=[('telnet', 'Telnet'), ('ssh', 'SSH')],
                             validators=[Required(u'请选择登陆方式')],
                             coerce=str,
                             )
    username = StringField('Username')
    password = PasswordField('Password')
    enable_password = PasswordField(
        'Enalbe Password', validators=[DataRequired()])
    submit = SubmitField(u'开始检查')

    def __init__(self, *args, **kwargs):
        super(ConfigForm, self).__init__(*args, **kwargs)
        self.device_model.choices = [(device.device_model, device.device_model)
                                     for device in DeviceType.query.order_by(DeviceType.id).all()]
