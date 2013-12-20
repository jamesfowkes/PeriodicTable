import elements
import string

def printElement(ele):
    print """\
            <div class=ele>
                <div class=dummy></div>
                <div class="content %s">
                    <span class=a>%d</span>
                    <span class=m>%s</span>
                    <div class=symbol>
                        <div class=symboltext>%s</div>
                    </div>
                </div>
            </div>""" % (ele.type, ele.a, ele.mass, ele.symbol)

def printKeyElement(id):
    print """\
            <div class="ele ele_key">
                <div class=dummy></div>
                <div class="content %s">
                    <div class=symbol>
                        <div class=symboltext>%s</div>
                    </div>
                </div>
            </div>""" % (id, string.replace(id, "_", " ").title())

def printSpacers(n):
    for _ in range(n):
            print """\
            <div class=blankele>&nbsp;
            </div>"""

def printEOR():
    print """\
        </div>"""

def printSOR():
    print """\
        <div class=row>"""

def printNormalElements():
    
    printSOR()
    
    for ele in elements.GetNormalElements():
        
        printElement(ele)
        
        printSpacers(ele.following_blanks)
            
        if ele.endofrow:
            printEOR()
            printSOR()
    
    printEOR()

def printBlankRows(n):
    for _ in range(n):
        printSOR()
        printSpacers(18)
        printEOR()
    
def outputTable():

    print "<div id=ptable>"
    printNormalElements()
    printBlankRows(1)
    printRareEarths()
    print "</div>"
    
def printRareEarths():
   
    printSOR()
    printSpacers(2)
    for ele in elements.GetLanthanides():
        printElement(ele)  
    printEOR()

    printSOR()    
    printSpacers(2)
    for ele in elements.GetActinides():
        printElement(ele)   
    printEOR()

def printFooter():    
    print """\
            <input type="range" min="0" max="100"></input>
        </body>
    </html>
    """

def printHeader():
    print """\
    <html>
        <head>
            <link rel="stylesheet" href="ptable.css" type="text/css" />
        </head>
        <body>
    """

def outputKey():
    
    for type in elements.GetTypes():
        printKeyElement(type)
    
def main():

    printHeader()

    outputTable()
    
    outputKey()
    
    printFooter()
    
main()