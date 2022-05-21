


from PyQt5 import QtCore, QtGui, QtWidgets
from asyncio.windows_utils import BUFSIZE
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pyplot as plt 
import networkx as nx
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import source


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(836, 720)
        self.graph_View = QtWidgets.QGraphicsView(Dialog)
        self.graph_View.setGeometry(QtCore.QRect(70, 19, 600, 381))
        self.graph_View.setObjectName("graph_View")
        self.node1_text = QtWidgets.QTextEdit(Dialog)
        self.node1_text.setGeometry(QtCore.QRect(310, 480, 71, 41))
        self.node1_text.setObjectName("node1_text")
        self.node2_text = QtWidgets.QTextEdit(Dialog)
        self.node2_text.setGeometry(QtCore.QRect(130, 480, 71, 41))
        self.node2_text.setObjectName("node2_text")
        self.weight_text = QtWidgets.QTextEdit(Dialog)
        self.weight_text.setGeometry(QtCore.QRect(210, 480, 71, 41))
        self.weight_text.setObjectName("weight_text")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(460, 480, 61, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(580, 480, 61, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(530, 420, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(190, 430, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(140, 460, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(230, 460, 51, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(320, 460, 51, 16))
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(470, 450, 51, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(580, 450, 61, 16))
        self.label_14.setObjectName("label_14")
        self.connect_button = QtWidgets.QPushButton(Dialog)
        self.connect_button.setGeometry(QtCore.QRect(200, 530, 131, 20))
        self.connect_button.setObjectName("connect_button")
        self.run_button = QtWidgets.QPushButton(Dialog)
        self.run_button.setGeometry(QtCore.QRect(420, 530, 81, 21))
        self.run_button.setObjectName("run_button")
        self.resetgraph_button = QtWidgets.QPushButton(Dialog)
        self.resetgraph_button.setGeometry(QtCore.QRect(600, 650, 111, 41))
        self.resetgraph_button.setObjectName("resetgraph_button")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(130, 630, 461, 91))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(350, 610, 51, 16))
        self.label_15.setObjectName("label_15")
        self.run_bell = QtWidgets.QPushButton(Dialog)
        self.run_bell.setGeometry(QtCore.QRect(420, 560, 81, 21))
        self.run_bell.setObjectName("run_bell")
        self.run_bell_2 = QtWidgets.QPushButton(Dialog)
        self.run_bell_2.setGeometry(QtCore.QRect(510, 560, 81, 21))
        self.run_bell_2.setObjectName("run_bell_2")
        self.run_bell_3 = QtWidgets.QPushButton(Dialog)
        self.run_bell_3.setGeometry(QtCore.QRect(510, 530, 81, 21))
        self.run_bell_3.setObjectName("run_bell_3")
        self.run_bell_4 = QtWidgets.QPushButton(Dialog)
        self.run_bell_4.setGeometry(QtCore.QRect(510, 590, 81, 21))
        self.run_bell_4.setObjectName("run_bell_4")
        self.run_kruskal = QtWidgets.QPushButton(Dialog)
        self.run_kruskal.setGeometry(QtCore.QRect(420, 590, 81, 21))
        self.run_kruskal.setObjectName("run_kruskal")
        self.run_bell_6 = QtWidgets.QPushButton(Dialog)
        self.run_bell_6.setGeometry(QtCore.QRect(600, 560, 111, 21))
        self.run_bell_6.setObjectName("run_bell_6")
        self.run_bell_7 = QtWidgets.QPushButton(Dialog)
        self.run_bell_7.setGeometry(QtCore.QRect(600, 530, 111, 21))
        self.run_bell_7.setObjectName("run_bell_7")
        self.connect_button_2 = QtWidgets.QPushButton(Dialog)
        self.connect_button_2.setGeometry(QtCore.QRect(10, 530, 91, 21))
        self.connect_button_2.setObjectName("connect_button_2")
        self.node2_text_2 = QtWidgets.QTextEdit(Dialog)
        self.node2_text_2.setGeometry(QtCore.QRect(20, 480, 71, 41))
        self.node2_text_2.setObjectName("node2_text_2")
        # self.G = nx.Graph()
        self.plot_canvas = PlotCanvas(self.graph_View)
        self.plot_canvas.setGeometry(QtCore.QRect(190, 30, 461, 301))
        self.plot_canvas.setObjectName("plot_canvas")
      
        self.retranslateUi(Dialog)  
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_12.setText(_translate("Dialog", "Run"))
        self.label_4.setText(_translate("Dialog", "Connect Nodes"))
        self.label_5.setText(_translate("Dialog", "Node 1"))
        self.label_6.setText(_translate("Dialog", "Weight"))
        self.label_7.setText(_translate("Dialog", "Node 2"))
        self.label_13.setText(_translate("Dialog", "Source"))
        self.label_14.setText(_translate("Dialog", "Destination"))
        self.connect_button.setText(_translate("Dialog", "Connect"))
        self.run_button.setText(_translate("Dialog", "Run_Dijkstra"))
        self.resetgraph_button.setText(_translate("Dialog", "Reset Graph"))
        self.label_15.setText(_translate("Dialog", "Reselt"))
        self.run_bell.setText(_translate("Dialog", "Run_Bell"))
        self.run_bell_2.setText(_translate("Dialog", "Run_DFS"))
        self.run_bell_3.setText(_translate("Dialog", "Run_BFS"))
        self.run_bell_4.setText(_translate("Dialog", "Run_Prim"))
        self.run_kruskal.setText(_translate("Dialog", "run_kruskal"))
        self.run_bell_6.setText(_translate("Dialog", "run_ford_fulkerson"))
        self.run_bell_7.setText(_translate("Dialog", "run_warshall"))
        self.connect_button_2.setText(_translate("Dialog", "Add Node"))


        # By inheriting the FigureCanvas class, this class is both a PyQt5 Qwidget and a Matplotlib FigureCanvas, which is the key to connecting pyqt5 and matplotlib

         
        
class PlotCanvas(FigureCanvas): 
    """Un élément d'interface utilisateur pour tracer le graphique de réseaux sur la fenêtre.
    """
    def __init__(self, parent=None):
        """Constructeur de la classe PlotCanvas.

        Arguments :
            parent (facultatif) : Le parent doit être un widget Qt. La valeur par défaut est None.
        """
        FigureCanvas.__init__(self)
        self.setParent(parent)
        self.figure = plt.figure()
        FigureCanvas.updateGeometry(self)
       

    def plot(self, G):
        """Tracer tous les noeuds et arêtes du graphe avec des étiquettes.

        Arguments :
            G (nx.Graph) : Graphe.
        """
        self.figure.clf()
        pos=nx.spring_layout(G, seed=42)

        
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw(G, pos, with_labels=True, font_size=11, node_size=150, node_color="r", font_color="w")
        self.draw_idle()

##################################


class GUI(QtWidgets.QWidget):
    alg="Dijkstra"
    """Classe principale de l'interface utilisateur graphique pour gérer les fonctions de l'interface utilisateur et du contrôleur.

    Arguments :
        QtWidgets.QMainWindow()
    """
    def __init__(self):
        """Constructeur de l'interface graphique.
        """
        super(GUI, self).__init__()
        self.algo = None
        self.setup_gui()
    def setup_gui(self):
        """Initialisateur de l'interface graphique.
        """
        self.form = Ui_Dialog()
        self.form.setupUi(self)
        self.G = nx.Graph()
        #Controllers
        self.form.connect_button_2.clicked.connect(self.add_new_node)
        self.form.connect_button.clicked.connect(self.connect_nodes)
        self.form.run_button.clicked.connect(self.run)
        self.form.resetgraph_button.clicked.connect(self.reset)
        self.form.run_bell.clicked.connect(self.run_Bell)
        self.form.run_bell_2.clicked.connect(self.Run_DFS)
        self.form.run_kruskal.clicked.connect(self.Run_kruskal)
        self.form.run_bell_3.clicked.connect(self.Run_BFS)
        # self.form.save_data.clicked.connect(self.save_data)
        # self.form.run_bell_4.clicked.connect(self.Run_Prim)
        # self.form.run_bell_6.clicked.connect(self.ford_fulkerson)
        # self.form.run_bell_7.clicked.connect(self.Run_warshall)
    def show_dialog(self, message):
        """Ouvrir une nouvelle fenêtre d'erreur avec un message d'erreur donné.

        Arguments :
            message (string) : texte de l'erreur.
        """
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()
    def add_new_node(self):
        """Ajout d'un nouveau nœud au graphique. 
        """
        new_node = str(self.form.node2_text_2.toPlainText())
        if not new_node:
            self.form.node2_text_2.clear()
            self.show_dialog("Empty argument.")
            return
        self.form.node2_text_2.clear()
        if self.G.has_node(new_node):
            self.show_dialog(f"{new_node} is already constructed.")
        else:
            self.G.add_node(new_node)
            self.form.plot_canvas.plot(self.G)    
    def connect_nodes(self):
        """Connecte deux noeuds avec un poids donné.
        """
        node1 = str(self.form.node1_text.toPlainText())
        node2 = str(self.form.node2_text.toPlainText())
        weight = str(self.form.weight_text.toPlainText())
        self.form.node1_text.clear()
        self.form.node2_text.clear()
        self.form.weight_text.clear()
        if not node1 or not node2 or not weight:      
            self.show_dialog("Argument vide")
            return
        try:
            weight = int(weight)
        except:
            self.show_dialog("Le poids doit être un nombre entier.")
            return

        if self.G.has_edge(node1, node2):
            self.show_dialog(f"Edge: {node1, node2} is already constructed.")
        else:
            self.G.add_edge(node1, node2, weight=weight)
            self.form.plot_canvas.plot(self.G)
    def setAlgo(self, algo):
        self.algo = algo
# les fonctions responsables de Run:
#Si je clique sur Run_Dijkstra
    def run(self):
         source = str(self.form.textEdit.toPlainText())
         target = str(self.form.textEdit_2.toPlainText())
         self.form.textEdit.clear()
         self.form.textEdit_2.clear()
         short=nx.dijkstra_path(self.G,source,target)
         result = f"le plus cours chemin entre {source} et {target} est: {short} "
         self.form.textEdit_3.setText(result)
#Si je clique sur Run_Bell         
    def run_Bell(self):
         source = str(self.form.textEdit.toPlainText())
         target = str(self.form.textEdit_2.toPlainText())
         self.form.textEdit.clear()
         self.form.textEdit_2.clear()
         bell=nx.bellman_ford_path(self.G,source,target,weight='weight')
         res = f" pour bellman le plus cours chemin  est: {bell} "
         self.form.textEdit_3.setText(res)
#Si je clique sur Run_kruskal
    def Run_kruskal(self):
         bell=nx.minimum_spanning_edges(self.G, weight='weight', data=True)
         edgelist=list(bell) # make a list of the edge
         res = f" l'arbre couvrant minimum (ACM) de notre graphe est{edgelist} "
         self.form.textEdit_3.setText(res)
#Si je clique sur Run_DFS
    def Run_DFS(self):
         source = str(self.form.textEdit.toPlainText())
         DF=nx.dfs_edges(self.G,source, depth_limit=None)
         ls=list(DF)
         res = f" le resultats de DFS est{ls} "
         self.form.textEdit_3.setText(res)
#Si je clique sur Run_BFS
    def Run_BFS(self):
        BF=nx.bfs_edges(self.G,source=None,reverse=False, depth_limit=None, sort_neighbors=None)
        ls=list(BF)
        res = f" le resultats  de BFS est{ls} "
        self.form.textEdit_3.setText(res)

#Si je clique sur Run_Prim
#Si je clique sur Run_warshall
#Si je clique sur Run_ford_fulkerson

#fin Run
    def reset(self):
        """Réinitialise le graphique existant.
        """
        self.G = nx.Graph()
        self.form.plot_canvas.plot(self.G)




