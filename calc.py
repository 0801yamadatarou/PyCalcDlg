from PyQt5 import QtWidgets, uic
import re

# 数字追加
def Insert0():#テキストエディットに0を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"0")
    
def Insert1():#テキストエディットに1を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"1")
    
def Insert2():#テキストエディットに2を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"2")
    
def Insert3():#テキストエディットに3を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"3")
    
def Insert4():#テキストエディットに4を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"4")
    
def Insert5():#テキストエディットに5を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"5")
    
def Insert6():#テキストエディットに6を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"6")
    
def Insert7():#テキストエディットに7を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"7")

def Insert8():#テキストエディットに8を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"8")

def Insert9():#テキストエディットに9を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"9")
    
# 記号ボタン入力
def InsertDivi():#テキストエディットに/を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"/")

def InsertAdd():#テキストエディットに+を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"+")
        
def InsertPoint():#テキストエディットに.を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+".")
    
def InsertSub():#テキストエディットに-を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"-")
    
def InsertMulti():#テキストエディットに*を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"*")
    
def InsertEqual():#テキストエディットに=を追加する
    textEditString=calcDlg.textEdit.toPlainText()
    calcDlg.textEdit.setPlainText(textEditString+"=")
    
def InsertClear():#テキストエディットクリアする
    calcDlg.textEdit.setPlainText("")
        
# 数式分割
def SplitNumber():#テキストエディットを文字列で分割
    formulaStr=calcDlg.textEdit.toPlainText()
    formulaSpliteInt=re.split('[/|+|-|*|=|-]', formulaStr)
    return formulaSpliteInt
    
def SplitSymbol():#テキストエディットを数字で分割
    formulaStr=calcDlg.textEdit.toPlainText()
    formulaSpliteSymbol=re.split('\d+', formulaStr)
    return formulaSpliteSymbol

# 計算処理
def Calculation():
    formulaSpliteInt=SplitNumber()
    formulaSpliteInt = [float(i) for i in formulaSpliteInt]
    formulaSpliteSymbol=SplitSymbol()
    while '' in formulaSpliteSymbol:formulaSpliteSymbol.remove('')
    while '.' in formulaSpliteSymbol:formulaSpliteSymbol.remove('.')
    count=0
    for symbolStr in formulaSpliteSymbol:
        if "+" in symbolStr:
            formulaSpliteInt[count+1]= formulaSpliteInt[count] + formulaSpliteInt[count+1]
        elif "-" in symbolStr:
            formulaSpliteInt[count+1]= formulaSpliteInt[count] - formulaSpliteInt[count+1]
        elif "*" in symbolStr:
            formulaSpliteInt[count+1]= formulaSpliteInt[count] * formulaSpliteInt[count+1]
        elif "/" in symbolStr:
            formulaSpliteInt[count+1]= formulaSpliteInt[count] / formulaSpliteInt[count+1]
        count=count+1
        
    formulaSpliteInt = [str(i) for i in formulaSpliteInt]
    calcDlg.textEdit.setPlainText(formulaSpliteInt[-1])



app = QtWidgets.QApplication([])  # アプリケーションを作成
ui_path = "ui"
calcDlg = uic.loadUi(f"{ui_path}/calc.ui")  # 作成したuiファイルを読み出して, ダイアログを作成

# 数字ボタン入力
calcDlg.pushCalc0Button.clicked.connect(Insert0)
calcDlg.pushCalc1Button.clicked.connect(Insert1)
calcDlg.pushCalc2Button.clicked.connect(Insert2)
calcDlg.pushCalc3Button.clicked.connect(Insert3)
calcDlg.pushCalc4Button.clicked.connect(Insert4)
calcDlg.pushCalc5Button.clicked.connect(Insert5)
calcDlg.pushCalc6Button.clicked.connect(Insert6)
calcDlg.pushCalc7Button.clicked.connect(Insert7)
calcDlg.pushCalc8Button.clicked.connect(Insert8)
calcDlg.pushCalc9Button.clicked.connect(Insert9)

# 記号ボタン入力
calcDlg.pushCalcDiviButton.clicked.connect(InsertDivi)
calcDlg.pushCalcAddButton.clicked.connect(InsertAdd)
calcDlg.pushCalcPointButton.clicked.connect(InsertPoint)
calcDlg.pushCalcSubButton.clicked.connect(InsertSub)
calcDlg.pushCalcMultiButton.clicked.connect(InsertMulti)

calcDlg.pushCalcEqualButton.clicked.connect(Calculation)

# 特殊ボタン
calcDlg.pushButton.clicked.connect(InsertClear)

if __name__ == "__main__":
    calcDlg.show()  # ダイアログ1を表示
    app.exec()   # 実行
    
