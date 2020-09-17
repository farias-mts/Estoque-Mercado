from tkinter import *
from controller import *

def notification(id_produto, produto, tipo, qtde):
    def show_notification():
        window_notification = Toplevel(root)
        window_notification.geometry('150x150')
        window_notification.resizable(False, False)
        text_notification = Label(
            window_notification,
            text='O Seguinte Produto foi cadastrado no código %d:\nNome do Produto: %s\nCategoria: %s\nQuantidade: %d'%(id_produto, produto, tipo, qtde)
        )
        window_notification.mainloop()
    frame_notification = Frame(
        back_frame3,
        bg='#ffffff',
        width=400,
        height=20
    )
    frame_notification.place(x=10, y=475)
    notification_product = Label(
        frame_notification,
        text = 'O produto foi cadastrado no código %d' %(id_produto),
        fg='#333'
    )
    notification_product.pack()
    notification_product.bind('<Button-1>', )


def clearFrame():
    for widget in back_frame3.winfo_children():
        widget.destroy()

def home(back_frame3):
    back_frame3.config(bg='#333')

def newType(back_frame3): 
    clearFrame()
    title_transaction = Label(
        back_frame3,
        text='Criar Categoria',
        font=('Calibri', '17', 'bold'),
        fg='#ffffff', 
        bg='#333'
    )
    title_transaction.place(x=150 ,y=60)

    label_type = Label(
        back_frame3,
        text='Categoria/Tipo',
        font=('Calibri', '14', 'bold'),
        fg='#ffffff',
        bg='#333'
    )
    label_type.place(x=15, y=120)

    type_box = Entry(
        back_frame3,
        width=20,
        font=('Calibre', '13'),
        fg='#333'
    )
    type_box.place(x=155 ,y=123)

    btn_executable = Button(
        back_frame3,
        text='Executar',
        font=('Calibre', '12'),
        bg='#ffffff',
        fg='#333',
        command=lambda:nova_categoria(type_box.get())
    )
    btn_executable.place(x=265, y=170)

def newProduct(back_frame3):
    def selectType(event):
        def on_keyRelease(event):
            value = entry.get().lower()
            if value == '':
                filtro = dados
            else:
                filtro = []
                for item in dados:
                    if value in item.lower():
                        filtro.append(item)                   
            listbox_update(filtro)

        def listbox_update(filtro):
            listbox.delete(0, 'end')
            for item in filtro:
                listbox.insert('end', item)
        
        def on_select(event):
            category_box.delete(0, 'end')
            value = event.widget.get(event.widget.curselection())
            category_box.insert(0, value)
            pop.destroy()
            
        pop = Toplevel(root)
        pop.title('Selecionar Valor')
        pop.geometry('200x200')
        pop.resizable(False, False)
        pop.configure(bg='#333')
        
        pop_title = Label(
            pop,
            text='Selecionar Categoria',
            bg='#333',
            fg='#ffffff',
            font=('Calibri', '13', 'bold')
        )
        pop_title.pack()

        entry = Entry(
            pop,
            fg='#333',
            width=20
        )
        entry.pack()
        entry.bind('<KeyRelease>', on_keyRelease)

        listbox = Listbox(pop)
        listbox.pack()
        listbox.bind('<Double-Button-1>', on_select)
        dados = retornar_categorias()
        listbox_update(dados)
        pop.mainloop()

    clearFrame()
    title_transaction = Label(
        back_frame3,
        text='Cadastrar Novo Produto',
        font=('Calibri', '17', 'bold'),
        fg='#ffffff', 
        bg='#333'
    )
    title_transaction.place(x=115 ,y=60)

    label_productName = Label(
        back_frame3,
        text='Nome do Produto',
        font=('Calibri', '14', 'bold'),
        fg='#ffffff',
        bg='#333'
    )
    label_productName.place(x=15, y=120)

    label_category = Label(
        back_frame3,
        text='Categoria do Produto',
        font=('Calibri', '14', 'bold'),
        fg='#ffffff',
        bg='#333'
    )
    label_category.place(x=15, y=160)

    label_selectCategory = Label(
        back_frame3,
        text='O',
        font=('Calibri', '10'),
        bg='#F74747',
        fg='#333'
    )
    label_selectCategory.place(x=395, y=165)
    label_selectCategory.bind('<Button-1>', selectType)

    label_amount = Label(
        back_frame3,
        text='Quantidade',
        font=('Calibri', '14', 'bold'),
        fg='#ffffff',
        bg='#333'
    )
    label_amount.place(x=15, y=200)

    productName_box = Entry(
        back_frame3,
        width=20,
        font=('Calibre', '13'),
        fg='#333'
    )
    productName_box.place(x=205 ,y=123)

    category_box = Entry(
        back_frame3,
        width=20,
        font=('Calibre', '13'),
        fg='#333'
    )
    category_box.place(x=205 ,y=163)

    amount_box = Entry(
        back_frame3,
        width=20,
        font=('Calibre', '13'),
        fg='#333'
    )
    amount_box.place(x=205 ,y=203)

    btn_executable = Button(
        back_frame3,
        text='Executar',
        font=('Calibre', '12'),
        bg='#ffffff',
        fg='#333',
        command=lambda:novo_produto(productName_box.get(), category_box.get(), amount_box.get())
    )
    btn_executable.place(x=315, y=250)
    
def searchProduct(): 
    def result_search():
        def table():
            itens = len(results)
            x = 0
            for line in range(itens):
                for column in range(4):
                    value = results[x][column-1]
                    entry = Label(
                        frame_show_results, 
                        text=value,
                        font=('Calibri', '13'),
                        width=10
                    )
                    entry.grid(row=line, column=column)
                x+=1

        def back_search():
            clearFrame()
            searchProduct()
    
        value_box = str(productName_box.get())
        results = buscar_produto(value_box)  
        clearFrame()
        button_back = Button(
            back_frame3,
            text='Voltar',
            bg='#333',
            fg='#ffffff',
            command=back_search
        )
        button_back.place(x=30 ,y=60)

        label_title_result = Label(
            back_frame3,
            text='Resultado da Pesquisa',
            font=('Calibri', '15', 'bold'),
            bg='#333',
            fg='#ffffff'
        )
        label_title_result.place(x=105 ,y=60)

        frame_show_title = Frame(
            back_frame3,
            bg='#ffffff',
            width=384,
            height=28
        )
        frame_show_title.place(x=40, y=130)

        frame_show_results = Frame(
            back_frame3,
            bg='#ffffff',
            width=370,
            height=320
        )
        frame_show_results.place(x=40, y=159)

        column_codigo = Label(
            frame_show_title,
            text='Código',
            font=('Calibri', '14', 'bold'),
            bg='#F74747',
            fg='#ffffff',
            width=9
        )
        column_codigo.place(x=0, y=0)

        column_product = Label(
            frame_show_title,
            text='Produto',
            font=('Calibri', '14', 'bold'),
            bg='#F74747',
            fg='#ffffff',
            width=9
        )
        column_product.place(x=82, y=0)

        column_category = Label(
            frame_show_title,
            text='Categoria',
            font=('Calibri', '14', 'bold'),
            bg='#F74747',
            fg='#ffffff',
            width=9
        )
        column_category.place(x=178, y=0)

        column_amount = Label(
            frame_show_title,
            text='Quantidade',
            font=('Calibri', '14', 'bold'),
            bg='#F74747',
            fg='#ffffff',
            width=11
        )
        column_amount.place(x=274, y=0)
        table()

    clearFrame()
    title_transaction = Label(
        back_frame3,
        text='Buscar Produtos Cadastrados',
        font=('Calibri', '17', 'bold'),
        fg='#ffffff', 
        bg='#333'
    )
    title_transaction.place(x=75 ,y=60)

    label_type = Label(
        back_frame3,
        text='Nome do Produto',
        font=('Calibri', '14', 'bold'),
        fg='#ffffff',
        bg='#333'
    )
    label_type.place(x=15, y=120)

    productName_box = Entry(
        back_frame3,
        width=20,
        font=('Calibre', '13'),
        fg='#333'
    )
    productName_box.place(x=175 ,y=123)

    btn_executable = Button(
        back_frame3,
        text='Executar',
        font=('Calibre', '12'),
        bg='#ffffff',
        fg='#333',
        command=lambda:result_search()
    )
    btn_executable.place(x=285, y=170)


root = Tk()
root.title('Market')
root.geometry('600x500')
root.resizable(False, False)
root.configure(bg='#ffffff')

back_frame1 = Frame(
    root,
    bg='#F74747',
    width=150,
    height=500
)
back_frame1.place(x=0, y=0)
label_title = Label(
    back_frame1,
    text='Mercado',
    font=('Calibri', '14', 'bold'),
    bg='#F74747',
    fg='#ffffff'
)
label_title.place(x=35, y=5)

btn_newType = Button(
    back_frame1,
    text='Nova Categoria',
    font=('Calibri', '13', 'bold'),
    bg='#F74747',
    fg='#ffffff',
    command=lambda:newType(back_frame3)
)
btn_newType.config(borderwidth=0)
btn_newType.place(x=5, y=75)

btn_newProduct = Button(
    back_frame1,
    text='Novo Produto',
    font=('Calibri', '13', 'bold'),
    bg='#F74747',
    fg='#ffffff',
    command=lambda:newProduct(back_frame3)
)
btn_newProduct.config(borderwidth=0)
btn_newProduct.place(x=5, y=115)

btn_searchProduct = Button(
    back_frame1,
    text='Buscar Produto',
    font=('Calibri', '13', 'bold'),
    bg='#F74747',
    fg='#ffffff',
    command=lambda:searchProduct()
)
btn_searchProduct .config(borderwidth=0)
btn_searchProduct .place(x=5, y=155)

back_frame2 = Frame(
    root,
    bg='#ffffff',
    width=6,
    height=500
)
back_frame2.place(x=150, y=0)

back_frame3 = Frame(
    root,
    bg='#333',
    width=444,
    height=500,
)
back_frame3.place(x=156, y=0)

root.mainloop()
