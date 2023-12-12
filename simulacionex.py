class cursos:
    def __init__(self, id, nombre, creditos, añosdeestudio):
        self.id=id
        self.nombre =nombre
        self.creditos =creditos
        self.añosdeestudio =añosdeestudio
    def info(self):
        print(f'la ficha de estos cursos son {self.id}, {self.nombre}, {self.creditos}, {self.añosdeestudio}')
class alumno:
    def __init__(self, id, nombre, email):
        self.id=id
        self.nombre=nombre
        self.email=email
    def info(self):
        print(f'la matricula del alumno es {self.id}, {self.nombre}, {self.email}')
class matricula:
    def __init__(self, idmatricula, fechamatricula,idalumno,idcurso):
        self.idmatricula=idmatricula
        self.fechamatricula=fechamatricula
        self.idalumno=idalumno
        self.idcurso=idcurso


curso1=cursos(1,"SMIR",2500,2)
curso2=cursos(2, "DAM",4500,2)
curso3=cursos(3,"DAW",4500, 2)
alumno1=alumno(1,"Diego","diego.huerta@campusfp.es")
alumno2=alumno(2, "Andrea","andrea.huerta@campusfp.es")
alumno3=alumno(3,"Jose Luis","pepelu.huerta@campusfp.es")
matricula1=matricula(1,"20-12-2023",1,1)
matricula2=matricula(2,"10-10-2023",2,2)
matricula3=matricula(3,"5-11-2023",3,3)
curso1.info()
alumno1.info()
