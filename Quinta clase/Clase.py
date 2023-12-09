class Alumno:

#objeto
    def NombreCompleto(self,nombre,apellido):
        return nombre +" "+apellido

#instancia
alu = Alumno()
nombre =input("Nombre: ")
apellido =input("Apelllido: ")

print(alu.NombreCompleto("Nombre Completo: " + nombre, apellido))