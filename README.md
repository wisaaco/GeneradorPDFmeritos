# Generador de un PDF que incluye otros PDFs (méritos)

Esta herramienta se realizó para facilitar la tarea de crear un único fichero que englobe los certificados de los méritos en las solicitudes enviadas a la ANECA. 

La herramienta está implementada en Python 2.7 y también requiere latex. Las funcionalidades implementadas son bastante básicas, pero creo que puede extenderse (y mejorarse) fácilmente. Se ha testeado en OS High Sierra y en Windows 10.

## ¿cómo funciona?

### 1º) 
Los certificados han de organizarse en carpetas, donde el nombre de las carpeta representa la categoría ordenada del fichero PDF. El nombre de las carpeta está formado por un número inicial para preservar el orden y el texto deseado. Los certificados han de ser pdfs. 
 

Un ejemplo de estructura tipo:
```
1 OrganizacionCV (carpeta raíz)
  1. Méritos obligatorios
    1. Publicaciones científicas indexadas en JCR
    	myPaperJCR.pdf
    	my Sëcond Pàpér_2018.pdf
  2. Méritos complementarios
  3. Recibos de gas
  ...
```

### 2º) 
Los ficheros que van a generar el pdf están en la carpeta "2 GeneradorCV".



```
python GeneradorContenidosLatex.py
```

La ejecución del fichero "GeneradorContenidosLatex.py" crea contenido latex en el fichero "content.tex". Este contenido incluye múltiples secciones y sub-secciones de latex acorde a la jerarquía de directorios y entre las secciones incluye los certificados (\includepdf). Tan sólo soporta tres niveles de directorios (\section, \subsection, \subsubsection). Una mejora futura es incluir alguna notación para dar cabida a listas (itemize, enumerate).
Como el nombre de los certificados puede incluir caracteres no soportados por látex, se duplican y renombran los certificados en un directorio temporal. No es la solución más óptima pero funciona...

Ejemplo del contenido del fichero "content.tex" generado por el script de python:
```
\section{Méritos obligatorios}
\newpage\subsection{Publicaciones científicas indexadas en JCR}
\newpage\includepdf[pages=-,pagecommand={}]{temp/0.pdf}
\newpage\includepdf[pages=-,pagecommand={}]{temp/1.pdf}
```

### 3º) 
Finalmente, tan sólo debemos generar el documento PDF usando el documento principal llamado: main.tex. Os aconsejo utilizar vuestro editor de latex preferido. 

