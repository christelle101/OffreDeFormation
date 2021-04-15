install.packages("readr")
install.packages("networkD3")
install.packages("xlsx") 
install.packages("visNetwork")
install.packages("dplyr")
install.packages("stringr")
library("xlsx")
library(networkD3)
library(readr)
library(magrittr)
library(visNetwork)
library(dplyr)
library(stringr)


# le fichier e contient les relations entre les modules(les arcs) (2 colonnes : colonne from et colonne to) 
e = read.xlsx("~/Desktop/IDU 3/S6/Proj632/R/edges.xlsx", 1, header=TRUE, colClasses=NA,encoding = "utf_8")
# le fichier n contient les noeuds : (2 colonnes : colonne : identifiant et colonne : libellés des modules)
n = read.xlsx("~/Desktop/IDU 3/S6/Proj632/R/nod.xlsx", 1, header=TRUE, colClasses=NA,encoding = "utf_8")

A = visNetwork(n,e,height = "700px",width = "100%",main = "Lien entre les modules") %>% 
  visEdges(arrows = 'to')  %>% 
  visOptions(highlightNearest = TRUE, nodesIdSelection = TRUE) %>%
  visInteraction(navigationButtons = TRUE) %>% visLegend() %>%
  visGroups(groupname = "S5", color = "IndianRed") %>%
  visGroups(groupname = "S6", color = "LightCoral") %>%
  visGroups(groupname = "S7", color = "Salmon") %>%
  visGroups(groupname = "S8", color = "DarkSalmon") %>%
  visGroups(groupname = "S9", color = "LightSalmon") 

# pour sauvegarder le graph sous format html
saveNetwork(A,file = '~/Desktop/IDU 3/S6/Proj632/R/TestGraphO.html')































table(x$Source)
table(x$Target)

edges <- mutate(p, width = weight/5 + 1)
?visNetwork(n,edges) %>% visIgraphLayout(layout = "layout_with_fr") %>% visEdges(arrows = "middle")




network = ?simpleNetwork(p,linkColour = "pink", nodeColour = "# 3182bd",arrows())  



#######
el <- data.frame(from=as.numeric(factor(p$Source))-1, 
                 to=as.numeric(factor(p$Targets))-1 )
n = read.xlsx("~/Desktop/IDU 3/S6/Proj632/R/Nodes.xlsx", 1, header=TRUE, colClasses=NA,encoding = "utf_8")
nl <- cbind(idn=factor(n$Nod, levels=n$Nod), n)


forceNetwork(Links = el, Nodes = nl, Source="from", Target="to",
             NodeID = "idn",Group = "group",linkWidth = 1,
             linkColour = "#afafaf", fontSize=12, zoom=T, legend=T
             , opacity = 0.8)

#charge=-50,width = 100, height =50)
sort(MisLinks$value)
sort(MisNodes$size)

######################################"" test ##"""""""""


nodes <- data.frame(id = 1:10, 
                    label = paste("Node", 1:10)
                    )                 

head(nodes)


edges <- data.frame(from = sample(1:10, 8), to = sample(1:10, 8),
                    label = paste("Edge", 1:8))                   
head(edges)




visNetwork(nodes, edges, width = "100%")

head(p)
head(n)


visNetwork(n,p, width = "100%")

nodes <- data.frame(id = 1:3)
edges <- data.frame(from = c(1,2), to = c(1,3))
visNetwork(nodes, edges, width = "100%")
































