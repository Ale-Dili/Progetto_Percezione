from tkinter import *
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

root = Tk()
root.geometry('300x350')
root.eval('tk::PlaceWindow . center')

# Create a listbox
listbox = Listbox(root, width=40, height=20, selectmode=MULTIPLE)

df = pd.read_csv('country_density.csv', encoding='UTF-8')
for i  in range(len(df)):
    listbox.insert(i,df.values[i][1])
def selected_item():
    indexes=[]
    for i in listbox.curselection():
        indexes.append(i)
        listbox.select_clear(i)

    dataframe = df.iloc[indexes, :]

    # costruiamo il grafico a barre
    bar1 = px.bar(dataframe, x="Country", y="Density_(P/Km²)", color="Country",
                  orientation="v", hover_name="Country",
                  color_discrete_sequence=px.colors.qualitative.Dark2,
                  title="Densità di popolazione"
                  )
    # costruiamo il grafico a torta
    pie = px.pie(dataframe, values='Density_(P/Km²)', names='Country', title="Densità di popolazione")

    table = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df.Country, df.Density],
                   fill_color='lavender',
                   align='left'))
    ])

    # plottiamo entrambi i grafici
    bar1.show()
    pie.show()


btn = Button(root, text='Print Selected', command=selected_item)

# Placing the button and listbox
btn.pack(side='bottom')
listbox.pack()

root.mainloop()

