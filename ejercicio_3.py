class Alumno:
    
    def __init__(self,nombre,dni,hermanos = 0):
        self.nombre = nombre 
        self.dni = dni 
        self.legajo = self.generar_legajo(dni)
        self.hermanos = hermanos
        
    def generar_legajo(self,dni):
        primeros_digitos = str(dni)[:3]
        return('ALU_'+primeros_digitos)
    
    def completar_materias(self):
        self.materias = []
        materias = int(input("cantidad de materias: "))
        for x in range(materias):
            self.materias.append(input("Ingrese materia: "))
            
    def registrar_notas(self):
        aprobadas = []
        for materia in self.materias:
            nota = float(input("que nota sacate en "+materia+"?"))
            if nota >= 6:
                aprobadas.append(materia)
        for aprobada in aprobadas:
            self.materias.remove(aprobada)
            
        print("las materias que tiene pendiente son: " + str(self.materias))
        

alu = Alumno("Javier", 123774654, 5)
print(alu.legajo)
alu.completar_materias()
alu.registrar_notas()