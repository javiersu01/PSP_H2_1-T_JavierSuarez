import pymysql
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_data(query="SELECT * FROM ENCUESTA"):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="curso",
            database="ENCUESTAS"
        )
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print("Data fetched successfully:", rows)  # Debugging line
        return rows
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
        return []
    finally:
        if connection.open:
            cursor.close()
            connection.close()

def display_data(query="SELECT * FROM ENCUESTA"):
    data = fetch_data(query)
    if not data:
        messagebox.showinfo("No Data", "No data to display or an error occurred.")
        return
    for item in tree.get_children():
        tree.delete(item)
    for row in data:
        tree.insert("", "end", values=row)
    print("Data displayed successfully")  # Debugging line

def create_record():
    def save_record():
        try:
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="curso",
                database="ENCUESTAS"
            )
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO ENCUESTA (edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (entry_edad.get(), entry_sexo.get(), entry_bebidas_semana.get(), entry_cervezas_semana.get(), entry_bebidas_fin_semana.get(), entry_bebidas_destiladas_semana.get(), entry_vinos_semana.get(), entry_perdidas_control.get(), entry_diversion_dependencia_alcohol.get(), entry_problemas_digestivos.get(), entry_tension_alta.get(), entry_dolor_cabeza.get())
            )
            connection.commit()
            messagebox.showinfo("Success", "Record created successfully")
            display_data()
            form.destroy()
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"Error creating record: {e}")
        finally:
            if connection.open:
                cursor.close()
                connection.close()

    form = tk.Toplevel(root)
    form.title("Crear Registro")

    tk.Label(form, text="Edad").grid(row=0, column=0)
    entry_edad = tk.Entry(form)
    entry_edad.grid(row=0, column=1)

    tk.Label(form, text="Sexo").grid(row=1, column=0)
    entry_sexo = tk.Entry(form)
    entry_sexo.grid(row=1, column=1)

    tk.Label(form, text="Bebidas Semana").grid(row=2, column=0)
    entry_bebidas_semana = tk.Entry(form)
    entry_bebidas_semana.grid(row=2, column=1)

    tk.Label(form, text="Cervezas Semana").grid(row=3, column=0)
    entry_cervezas_semana = tk.Entry(form)
    entry_cervezas_semana.grid(row=3, column=1)

    tk.Label(form, text="Bebidas Fin Semana").grid(row=4, column=0)
    entry_bebidas_fin_semana = tk.Entry(form)
    entry_bebidas_fin_semana.grid(row=4, column=1)

    tk.Label(form, text="Bebidas Destiladas Semana").grid(row=5, column=0)
    entry_bebidas_destiladas_semana = tk.Entry(form)
    entry_bebidas_destiladas_semana.grid(row=5, column=1)

    tk.Label(form, text="Vinos Semana").grid(row=6, column=0)
    entry_vinos_semana = tk.Entry(form)
    entry_vinos_semana.grid(row=6, column=1)

    tk.Label(form, text="Perdidas Control").grid(row=7, column=0)
    entry_perdidas_control = tk.Entry(form)
    entry_perdidas_control.grid(row=7, column=1)

    tk.Label(form, text="Diversion Dependencia Alcohol").grid(row=8, column=0)
    entry_diversion_dependencia_alcohol = tk.Entry(form)
    entry_diversion_dependencia_alcohol.grid(row=8, column=1)

    tk.Label(form, text="Problemas Digestivos").grid(row=9, column=0)
    entry_problemas_digestivos = tk.Entry(form)
    entry_problemas_digestivos.grid(row=9, column=1)

    tk.Label(form, text="Tension Alta").grid(row=10, column=0)
    entry_tension_alta = tk.Entry(form)
    entry_tension_alta.grid(row=10, column=1)

    tk.Label(form, text="Dolor Cabeza").grid(row=11, column=0)
    entry_dolor_cabeza = tk.Entry(form)
    entry_dolor_cabeza.grid(row=11, column=1)

    btn_save = tk.Button(form, text="Guardar", command=save_record)
    btn_save.grid(row=12, columnspan=2)

def update_record():
    try:
        selected_item = tree.selection()[0]
        selected_values = tree.item(selected_item, 'values')
        selected_id = selected_values[0]

        def save_update():
            try:
                connection = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="curso",
                    database="ENCUESTAS"
                )
                cursor = connection.cursor()
                cursor.execute(
                    "UPDATE ENCUESTA SET edad = %s, Sexo = %s, BebidasSemana = %s, CervezasSemana = %s, BebidasFinSemana = %s, BebidasDestiladasSemana = %s, VinosSemana = %s, PerdidasControl = %s, DiversionDependenciaAlcohol = %s, ProblemasDigestivos = %s, TensionAlta = %s, DolorCabeza = %s WHERE idEncuesta = %s",
                    (entry_edad.get(), entry_sexo.get(), entry_bebidas_semana.get(), entry_cervezas_semana.get(), entry_bebidas_fin_semana.get(), entry_bebidas_destiladas_semana.get(), entry_vinos_semana.get(), entry_perdidas_control.get(), entry_diversion_dependencia_alcohol.get(), entry_problemas_digestivos.get(), entry_tension_alta.get(), entry_dolor_cabeza.get(), selected_id)
                )
                connection.commit()
                messagebox.showinfo("Success", "Record updated successfully")
                display_data()
                form.destroy()
            except pymysql.MySQLError as e:
                messagebox.showerror("Database Error", f"Error updating record: {e}")
            finally:
                if connection.open:
                    cursor.close()
                    connection.close()

        form = tk.Toplevel(root)
        form.title("Actualizar Registro")

        tk.Label(form, text="Edad").grid(row=0, column=0)
        entry_edad = tk.Entry(form)
        entry_edad.grid(row=0, column=1)
        entry_edad.insert(0, selected_values[1])

        tk.Label(form, text="Sexo").grid(row=1, column=0)
        entry_sexo = tk.Entry(form)
        entry_sexo.grid(row=1, column=1)
        entry_sexo.insert(0, selected_values[2])

        tk.Label(form, text="Bebidas Semana").grid(row=2, column=0)
        entry_bebidas_semana = tk.Entry(form)
        entry_bebidas_semana.grid(row=2, column=1)
        entry_bebidas_semana.insert(0, selected_values[3])

        tk.Label(form, text="Cervezas Semana").grid(row=3, column=0)
        entry_cervezas_semana = tk.Entry(form)
        entry_cervezas_semana.grid(row=3, column=1)
        entry_cervezas_semana.insert(0, selected_values[4])

        tk.Label(form, text="Bebidas Fin Semana").grid(row=4, column=0)
        entry_bebidas_fin_semana = tk.Entry(form)
        entry_bebidas_fin_semana.grid(row=4, column=1)
        entry_bebidas_fin_semana.insert(0, selected_values[5])

        tk.Label(form, text="Bebidas Destiladas Semana").grid(row=5, column=0)
        entry_bebidas_destiladas_semana = tk.Entry(form)
        entry_bebidas_destiladas_semana.grid(row=5, column=1)
        entry_bebidas_destiladas_semana.insert(0, selected_values[6])

        tk.Label(form, text="Vinos Semana").grid(row=6, column=0)
        entry_vinos_semana = tk.Entry(form)
        entry_vinos_semana.grid(row=6, column=1)
        entry_vinos_semana.insert(0, selected_values[7])

        tk.Label(form, text="Perdidas Control").grid(row=7, column=0)
        entry_perdidas_control = tk.Entry(form)
        entry_perdidas_control.grid(row=7, column=1)
        entry_perdidas_control.insert(0, selected_values[8])

        tk.Label(form, text="Diversion Dependencia Alcohol").grid(row=8, column=0)
        entry_diversion_dependencia_alcohol = tk.Entry(form)
        entry_diversion_dependencia_alcohol.grid(row=8, column=1)
        entry_diversion_dependencia_alcohol.insert(0, selected_values[9])

        tk.Label(form, text="Problemas Digestivos").grid(row=9, column=0)
        entry_problemas_digestivos = tk.Entry(form)
        entry_problemas_digestivos.grid(row=9, column=1)
        entry_problemas_digestivos.insert(0, selected_values[10])

        tk.Label(form, text="Tension Alta").grid(row=10, column=0)
        entry_tension_alta = tk.Entry(form)
        entry_tension_alta.grid(row=10, column=1)
        entry_tension_alta.insert(0, selected_values[11])

        tk.Label(form, text="Dolor Cabeza").grid(row=11, column=0)
        entry_dolor_cabeza = tk.Entry(form)
        entry_dolor_cabeza.grid(row=11, column=1)
        entry_dolor_cabeza.insert(0, selected_values[12])

        btn_save = tk.Button(form, text="Guardar", command=save_update)
        btn_save.grid(row=12, columnspan=2)

    except IndexError:
        messagebox.showerror("Selection Error", "No record selected")

def delete_record():
    try:
        selected_item = tree.selection()[0]
        selected_id = tree.item(selected_item, 'values')[0]
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="curso",
            database="ENCUESTAS"
        )
        cursor = connection.cursor()
        cursor.execute("DELETE FROM ENCUESTA WHERE idEncuesta = %s", (selected_id,))
        connection.commit()
        messagebox.showinfo("Success", "Record deleted successfully")
        display_data()
    except IndexError:
        messagebox.showerror("Selection Error", "No record selected")
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", f"Error deleting record: {e}")
    finally:
        if connection.open:
            cursor.close()
            connection.close()

def filter_data():
    def apply_filter():
        conditions = []
        if entry_edad.get():
            conditions.append(f"edad = {entry_edad.get()}")
        if entry_sexo.get():
            conditions.append(f"Sexo = '{entry_sexo.get()}'")
        if entry_bebidas_semana.get():
            conditions.append(f"BebidasSemana = {entry_bebidas_semana.get()}")
        if entry_cervezas_semana.get():
            conditions.append(f"CervezasSemana = {entry_cervezas_semana.get()}")
        if entry_bebidas_fin_semana.get():
            conditions.append(f"BebidasFinSemana = {entry_bebidas_fin_semana.get()}")
        if entry_bebidas_destiladas_semana.get():
            conditions.append(f"BebidasDestiladasSemana = {entry_bebidas_destiladas_semana.get()}")
        if entry_vinos_semana.get():
            conditions.append(f"VinosSemana = {entry_vinos_semana.get()}")
        if entry_perdidas_control.get():
            conditions.append(f"PerdidasControl = {entry_perdidas_control.get()}")
        if entry_diversion_dependencia_alcohol.get():
            conditions.append(f"DiversionDependenciaAlcohol = {entry_diversion_dependencia_alcohol.get()}")
        if entry_problemas_digestivos.get():
            conditions.append(f"ProblemasDigestivos = {entry_problemas_digestivos.get()}")
        if entry_tension_alta.get():
            conditions.append(f"TensionAlta = {entry_tension_alta.get()}")
        if entry_dolor_cabeza.get():
            conditions.append(f"DolorCabeza = {entry_dolor_cabeza.get()}")

        query = "SELECT * FROM ENCUESTA"
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        if sort_by.get():
            query += f" ORDER BY {sort_by.get()}"

        display_data(query)
        form.destroy()

    form = tk.Toplevel(root)
    form.title("Filtrar Datos")

    tk.Label(form, text="Edad").grid(row=0, column=0)
    entry_edad = tk.Entry(form)
    entry_edad.grid(row=0, column=1)

    tk.Label(form, text="Sexo").grid(row=1, column=0)
    entry_sexo = tk.Entry(form)
    entry_sexo.grid(row=1, column=1)

    tk.Label(form, text="Bebidas Semana").grid(row=2, column=0)
    entry_bebidas_semana = tk.Entry(form)
    entry_bebidas_semana.grid(row=2, column=1)

    tk.Label(form, text="Cervezas Semana").grid(row=3, column=0)
    entry_cervezas_semana = tk.Entry(form)
    entry_cervezas_semana.grid(row=3, column=1)

    tk.Label(form, text="Bebidas Fin Semana").grid(row=4, column=0)
    entry_bebidas_fin_semana = tk.Entry(form)
    entry_bebidas_fin_semana.grid(row=4, column=1)

    tk.Label(form, text="Bebidas Destiladas Semana").grid(row=5, column=0)
    entry_bebidas_destiladas_semana = tk.Entry(form)
    entry_bebidas_destiladas_semana.grid(row=5, column=1)

    tk.Label(form, text="Vinos Semana").grid(row=6, column=0)
    entry_vinos_semana = tk.Entry(form)
    entry_vinos_semana.grid(row=6, column=1)

    tk.Label(form, text="Perdidas Control").grid(row=7, column=0)
    entry_perdidas_control = tk.Entry(form)
    entry_perdidas_control.grid(row=7, column=1)

    tk.Label(form, text="Diversion Dependencia Alcohol").grid(row=8, column=0)
    entry_diversion_dependencia_alcohol = tk.Entry(form)
    entry_diversion_dependencia_alcohol.grid(row=8, column=1)

    tk.Label(form, text="Problemas Digestivos").grid(row=9, column=0)
    entry_problemas_digestivos = tk.Entry(form)
    entry_problemas_digestivos.grid(row=9, column=1)

    tk.Label(form, text="Tension Alta").grid(row=10, column=0)
    entry_tension_alta = tk.Entry(form)
    entry_tension_alta.grid(row=10, column=1)

    tk.Label(form, text="Dolor Cabeza").grid(row=11, column=0)
    entry_dolor_cabeza = tk.Entry(form)
    entry_dolor_cabeza.grid(row=11, column=1)

    tk.Label(form, text="Ordenar Por").grid(row=12, column=0)
    sort_by = ttk.Combobox(form, values=["edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"])
    sort_by.grid(row=12, column=1)

    btn_apply = tk.Button(form, text="Aplicar", command=apply_filter)
    btn_apply.grid(row=13, columnspan=2)

# Create the main window
root = tk.Tk()
root.title("Ventana de Prueba")
root.geometry("1200x600")

# Create the Treeview to display data
columns = ("idEncuesta", "edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza")
tree = ttk.Treeview(root, columns=columns, show='headings')

# Configure column headers
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(fill=tk.BOTH, expand=True)

# Create buttons for create, update, delete, filter, and load data operations
btn_create = tk.Button(root, text="Crear", command=create_record)
btn_create.pack(side=tk.LEFT, padx=10, pady=10)

btn_update = tk.Button(root, text="Actualizar", command=update_record)
btn_update.pack(side=tk.LEFT, padx=10, pady=10)

btn_delete = tk.Button(root, text="Eliminar", command=delete_record)
btn_delete.pack(side=tk.LEFT, padx=10, pady=10)

btn_filter = tk.Button(root, text="Filtrar", command=filter_data)
btn_filter.pack(side=tk.LEFT, padx=10, pady=10)

btn_load = tk.Button(root, text="Cargar Datos", command=display_data)
btn_load.pack(side=tk.LEFT, padx=10, pady=10)

def export_to_excel():
    data = fetch_data()
    if not data:
        return
    df = pd.DataFrame(data,
                      columns=["idEncuesta", "edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana",
                               "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl",
                               "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"])
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                             filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    if file_path:
        df.to_excel(file_path, index=False)
        messagebox.showinfo("Success", "Data exported successfully")


def visualize_data():
    data = fetch_data()
    if not data:
        return
    df = pd.DataFrame(data,
                      columns=["idEncuesta", "edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana",
                               "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl",
                               "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"])

    def plot_graph():
        graph_type = graph_type_var.get()
        if graph_type == "Barras":
            df.groupby('edad')['BebidasSemana'].mean().plot(kind='bar')
        elif graph_type == "Pastel":
            df['Sexo'].value_counts().plot(kind='pie')
        elif graph_type == "Líneas":
            df.groupby('edad')['BebidasSemana'].mean().plot(kind='line')
        plt.show()

    form = tk.Toplevel(root)
    form.title("Visualizar Datos")

    tk.Label(form, text="Tipo de Gráfico").grid(row=0, column=0)
    graph_type_var = tk.StringVar()
    graph_type_menu = ttk.Combobox(form, textvariable=graph_type_var, values=["Barras", "Pastel", "Líneas"])
    graph_type_menu.grid(row=0, column=1)

    btn_plot = tk.Button(form, text="Generar Gráfico", command=plot_graph)
    btn_plot.grid(row=1, columnspan=2)


# Add buttons for exporting to Excel and visualizing data
btn_export = tk.Button(root, text="Exportar a Excel", command=export_to_excel)
btn_export.pack(side=tk.LEFT, padx=10, pady=10)

btn_visualize = tk.Button(root, text="Visualizar Datos", command=visualize_data)
btn_visualize.pack(side=tk.LEFT, padx=10, pady=10)

# Call display_data() to show the data when the application starts
display_data()

# Run the Tkinter event loop
root.mainloop()