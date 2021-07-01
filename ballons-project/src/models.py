from app import db, ma
#from sqlalchemy import Column, Integer, String

'''
class Inventory(db.Model):
    __tablename__='Inventory'

    id = Column(Integer, primary_key=True,autoincrement=True)
    weight = Column(Integer)

    def __init__(self, weight=0):
        self.weight = weight
        
    def __repr__(self):
        return "<Inventory(weight='%d')>" % (self.weight)
'''

class Transaccion(db.Model):
    __tablename__='Transaccion'
    IDNumeroTransacicon = db.Column(db.String(50), primary_key=True, nullable=False)
    Estado = db.Column(db.String(10))
    ID_Tipo_transaccion = db.Column(db.String(50), nullable=False)

    def __init__(self, IDNumeroTransaccion=None, Estado=None, ID_Tipo_transaccion=None):
        self.IDNumeroTransaccion = IDNumeroTransaccion
        self.Estado = Estado
        self.ID_Tipo_transaccion = ID_Tipo_transaccion

    def __repr__(self):
        return '<Transaccion %r>' % self.IDNumeroTransaccion


class UsuarioTransaccion(db.Model):
    __tablename__='UsuarioTransaccion'
    FechaHora = db.Column(db.DateTime, primary_key=True, nullable=False)
    PesoLimpio = db.Column(db.Float, nullable=True)
    PesoSucio = db.Column(db.Float, nullable=True)
    PorcentajePinchadoLimpio= db.Column(db.Float, nullable=True)
    PorcentajePinchadoSucio = db.Column(db.Float, nullable=True)
    Scrap = db.Column(db.Float, nullable=True)
    ID_Usuario = db.Column(db.String(50), nullable=False)
    ID_Maquina = db.Column(db.String(50), nullable=False)
    ID_Producto = db.Column(db.String(50), nullable=False)
    IDTransaccion = db.Column(db.String(50), nullable=False)
    ID_Balanza = db.Column(db.String(50), nullable=False)

    def __init__(self, FechaHora=None, PesoLimpio=None, PesoSucio=None, PorcentajePinchadoLimpio=None, PorcentajePinchadoSucio=None, Scrap=None, ID_Usuario=None, ID_Maquina=None, ID_Producto=None, ID_Transaccion=None, ID_Balanza=None):
        self.FechaHora = FechaHora 
        self.PesoLimpio = PesoLimpio
        self.PesoSucio = PesoSucio
        self.PorcentajePinchadoLimpio = PorcentajePinchadoLimpio
        self.PorcentajePinchadoSucio = PorcentajePinchadoSucio
        self.Scrap = Scrap
        self.ID_Usuario = ID_Usuario
        self.ID_Maquina = ID_Maquina
        self.ID_Producto = ID_Producto
        self.ID_Transaccion = ID_Transaccion
        self.ID_Balanza = ID_Balanza

    def __repr__(self):
        return '<UsuarioTransaccion %r>' % self.FechaHora


class UsuarioTransaccionSchema(ma.Schema):
    class Meta:
        fields = ('IDNumeroTransaccion','ID_Tipo_transaccion')

class UsuarioTransaccionSchema(ma.Schema):
    class Meta:
        fields = ('FechaHora','PesoLimpio','PesoSucio','Scrap','ID_Usuario','ID_Producto','ID_Transaccion','ID_Balanza')

