#Importando Bilbiotecas   
from PySimpleGUI import PySimpleGUI as pg   
from tkinter import *  
from tkinter import messagebox  
from abc import ABC, abstractmethod 
import subprocess



#Adicionando um Tema para a Tela GUI 
pg.theme('SandyBeach')   
  

# Estruturando o Layout
layout = [
    
    [pg.Text('INFORME SEU NOME:', size =(18, 1)), pg.InputText()],
    [pg.Text('QUAL SUA RELAÇÂO COM A FATEC:'), pg.Combo(["Aluno", "Professor", "Cordenador","Diretor","Administrativo", "Vestibulando","Outro"])],
    [pg.Submit(), pg.Cancel()]
    
]
  
#Lendo valores e eventos
window = pg.Window('PORTARIA DA FATEC ZONA SUL', layout)
event, values = window.read() 


#Loop para criação de chamadas
def loop():
 msg_box =  messagebox.askquestion("PORTARIA DA FATEC INFORMA", "GOSTARIA DE UMA NOVA CHAMADA?")
 if msg_box == 'yes':
    subprocess.run("python GUI.py", shell=True) 
 else:
    window.close()
  

  
#Classe Abstrata Fatec
class Fatec(ABC):
 @abstractmethod
 def apresentar(self, nome):
  pass

# Subclasse de FATEC
class Aluno(Fatec):
 def apresentar(self, nome,relacao_pessoa):
    messagebox.showinfo("PORTARIA DA FATEC INFORMA", nome + " tem relação com a instituição como " + relacao_pessoa)  
    loop()
    return f"{nome} tem relação com a instituição como {relacao_pessoa}"
   
    
# Subclasse de FATEC
class Professor(Fatec):
 def apresentar(self,nome, relacao_pessoa):
     messagebox.showinfo("PORTARIA DA FATEC INFORMA", nome + " tem relação com a instituição como " + relacao_pessoa)  
     loop()
     return f"{nome} tem relação com a instituição como {relacao_pessoa}"


# Subclasse de FATEC
class Cordenador(Fatec):
 def apresentar(self, nome, relacao_pessoa):
      messagebox.showinfo("PORTARIA DA FATEC INFORMA", nome + " tem relação com a instituição como " + relacao_pessoa)   
      loop()
      return f"{nome} tem relação com a instituição como {relacao_pessoa}"
 
 # Subclasse de FATEC
class Diretor(Fatec):
 def apresentar(self, nome, relacao_pessoa):
      messagebox.showinfo("PORTARIA DA FATEC INFORMA", nome + " tem relação com a instituição como " + relacao_pessoa)  
      loop() 
      return f"{nome} tem relação com a instituição como {relacao_pessoa}"
 
 # Subclasse de FATEC
class Administrativo(Fatec):
 def apresentar(self, nome, relacao_pessoa):
      messagebox.showinfo("PORTARIA DA FATEC INFORMA", nome + " tem relação com a instituição como " + relacao_pessoa)   
      loop() 
      return f"{nome} tem relação com a instituição como {relacao_pessoa}"
 
 # Subclasse de FATEC
class Vestibulando(Fatec):
 def apresentar(self, nome, relacao_pessoa):
      messagebox.showinfo("PORTARIA DA FATEC INFORMA", nome + " tem relação com a instituição como " + relacao_pessoa)   
      loop() 
      return f"{nome} tem relação com a instituição como {relacao_pessoa}"
 

#ClasseFactoryMethod para delegar as instancias 
class CriaPortaria:
 
 def Criar_Chamada(self, nome,relacao_pessoa):
   
  if relacao_pessoa == "Aluno":
   return Aluno()
  elif relacao_pessoa == "Professor":
   return Professor()
  elif relacao_pessoa == "Cordenador":
   return Cordenador() 
  elif relacao_pessoa == "Diretor":
    return Diretor()
  elif relacao_pessoa == "Administrativo": 
    return Administrativo()
  elif relacao_pessoa == "Vestibulando":
    return Vestibulando()
  else:
   messagebox.showinfo("PORTARIA DA FATEC INFORMA", nome + " não tem nenhuma relação com a instituição, acompanhar até a secretaria")  
   loop()

#Evento de clicar no botao submeter
if event == 'Submit':

     Cria_Portaria = CriaPortaria()
     nome = values[0]
     relacao_pessoa = values[1]
     usuario = Cria_Portaria.Criar_Chamada(nome,relacao_pessoa)  
     print(usuario.apresentar(nome, relacao_pessoa)) 