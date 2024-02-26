class Empleado:
    def __init__(self, dni, nombre, apellido, anio_ingreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso

class EmpleadoConSalarioFijo(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, sueldo_basico):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.sueldo_basico = sueldo_basico       

    def calcular_salario(self):
        anios_en_empresa = 2024 - self.anio_ingreso
        if anios_en_empresa < 2:
            return self.sueldo_basico
        elif 2 <= anios_en_empresa <= 5:
            return self.sueldo_basico * 1.05
        else:
            return self.sueldo_basico * 1.1

    def mostrarSalario(self):
        salario = self.calcular_salario()
        print(f"{self.nombre} {self.apellido}: {salario}")


class EmpleadoComision(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, salario_minimo, clientes_captados, monto_por_cliente):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    def calcular_salario(self):
        salario = self.clientes_captados * self.monto_por_cliente
        return max(salario, self.salario_minimo)
    
    def mostrarSalario(self):
        salario = self.calcular_salario()
        print(f"{self.nombre} {self.apellido}: {salario}")

    @staticmethod
    def empleado_con_mas_clientes(*empleados):
        max_clientes = 0
        empleado_con_mas_clientes = None
        for empleado in empleados:
            if isinstance(empleado, EmpleadoComision) and empleado.clientes_captados > max_clientes:
                max_clientes = empleado.clientes_captados
                empleado_con_mas_clientes = empleado
        return empleado_con_mas_clientes   


empleado_fijo_1 = EmpleadoConSalarioFijo("34132994", "Ricardo", "Albornoz", 2018, 720000)
empleado_fijo_1.mostrarSalario()

empleado_comision_1 = EmpleadoComision("37811515", "Facundo", "Juarez", 2010, 500000, 20, 20000)
empleado_comision_2 = EmpleadoComision("37811514", "Pepe", "Juarez", 2005, 5000000, 40, 20000)
empleado_comision_3 = EmpleadoComision("37811513", "Pedro", "Lopez", 2020, 500000, 60, 20000)
empleado_comision_4 = EmpleadoComision("37811512", "Arnaldo", "Paredes", 2024, 500000, 35, 20000)
empleado_comision_5 = EmpleadoComision("37811511", "Juan", "Perez", 2022, 500000, 34, 20000)
empleado_comision_6 = EmpleadoComision("37811510", "Ignacio", "Salcedo", 2022, 500000, 41, 20000)
empleado_comision_7 = EmpleadoComision("37811509", "Esteban", "Quito", 2020, 500000, 10, 20000)
empleado_comision_8 = EmpleadoComision("37811508", "Fernando", "Walker", 2018, 500000, 5, 20000)

empleado_con_mas_clientes = EmpleadoComision.empleado_con_mas_clientes(empleado_comision_1, empleado_comision_2, empleado_comision_3, empleado_comision_4, empleado_comision_5, empleado_comision_6, empleado_comision_7, empleado_comision_8)
print(f"El empleado con más clientes captados es {empleado_con_mas_clientes.nombre} {empleado_con_mas_clientes.apellido} con {empleado_con_mas_clientes.clientes_captados} clientes.")