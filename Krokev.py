import math

class Krokev:
    def __init__(
                 self, sirka_budovy: float,
                 stoupani: str,
                 tloustka_hrebenoveho_tramu: float,
                 vyska_hrebenoveho_tramu: float,
                 sirka_krokve: float,
                 delka_sedla: float,
                 presah_strechy: float
                ):
        """
        param sirka_budovy = float (m)
        param stoupani = string (přiklad 4:12 inch (palců))
        param tloustka_hrebenoveho_tramu = float (cm)
        paranm vyska_hrebenoveho_tramu = float (cm)
        param sirka_krokve = float (cm)
        param delka_sedla = float (cm)
        param presah_strechy = float (cm)
        """
        if not isinstance(sirka_budovy, float):
            raise TypeError("sirka_budovy musí být desetinné číslo (float)")
        
        if not isinstance(stoupani, str):
             raise TypeError("stoupani musí být řetězec (string)")
        
        if not isinstance(tloustka_hrebenoveho_tramu, float):
            raise TypeError("tloustka_hrebenoveho_tramu musí být desetinné číslo (float)")
            
        if not isinstance(vyska_hrebenoveho_tramu, float):
            raise TypeError("vyska_hrebenoveho_tramu musí být desetinné číslo (float)")
            
        if not isinstance(sirka_krokve, float):
            raise TypeError("sirka_krokve musí být desetinné číslo (float)")
        
        if not isinstance(delka_sedla, float):
            raise TypeError("delka_sedla musí být desetinné číslo (float)")
            
        if not isinstance(presah_strechy, float):
            raise TypeError("presah_strechy musí být desetinné číslo (float)")
                
        self.sirka_budovy = sirka_budovy
        self.stoupani = stoupani
        self.tloustka_hrebenoveho_tramu = tloustka_hrebenoveho_tramu
        self.sirka_krokve = sirka_krokve
        self.delka_sedla = delka_sedla
        self.presah_strechy = presah_strechy
    
    def getRatio(self)->list:
        """
        Vrátí převedený poměr z palců na základní jendotky.
        Např: 4:12 = 1:3
        
        rtype = list
        """
        input_ratio = self.stoupani.split(":")
        
        rise = float(input_ratio[0])
        run = float(input_ratio[1])
        run_ratio = run/run
        ratio = round(run/rise,2)
        return [run_ratio,ratio]
    
    def getRun(self)->float:
        """
        Vrátí hodnoru run.
        rtype = float
        """
        sirka_budovy_cm = self.sirka_budovy*100
        run = round((sirka_budovy_cm-self.tloustka_hrebenoveho_tramu)/2,1)
        return run
    
    def getRise(self)->float:
        """
        Vrátí hodnoru rise.
        rtype = float
        """
        run = self.getRun()
        run_ratio = self.getRatio()[1]
        rise = round(run/run_ratio,1)
        return rise
    
    def getLineLength(self)->float:
        """
        Vrátí délku úhlové čáry na krokvi.
        @return: float
        """
        run_ratio = self.getRatio()[1]
        run = self.sirka_krokve
        rise = round((run/run_ratio),1)
        line_length = round(math.sqrt(run**2+rise**2),1)
        return line_length
    
    def getSeatDepth(self)->float:
        """
        Vrátí hodnotu hlouobky sedla (zářezu pro sedlo).
        rtype: float
        """
        run_ratio = self.getRatio()[1]
        run = self.sirka_krokve
        rise = round((run/run_ratio),1)
        line_length = run**2+rise**2
        line_length = round(math.sqrt(line_length),1)
        rise_sedla_teoreticky = round(self.delka_sedla/run_ratio,1)
        if rise_sedla_teoreticky<=(line_length/3):
            return rise_sedla_teoreticky
        else:
            return round(line_length/3,1)
   
    def getRealRise(self)->float:
        """
        Vrátí skutečnou stavební výšku hřebene.
        rtype: float
        """
        line_length = self.getLineLength()
        rise = self.getRise()
        seat_depth = self.getSeatDepth()
        result = round(rise + (line_length-seat_depth),1)
        return result
        
    def getRafterLength(self)->float:
        """
        Vrátí délku krokve bez přesahu.
        @return: float
        """
        run = self.getRun()
        rise = self.getRise()
        result = round(math.sqrt(run**2+rise**2),1)
        return result
    
    def getOverhang(self)->float:
        """
        Vrátí délku přesahu krokve.
        @return: float
        """
        run_ratio = self.getRatio()[1]
        rise = self.presah_strechy/run_ratio
        run = self.presah_strechy
        overhang_length = round(math.sqrt(rise**2+run**2),1)
        return overhang_length
    
    def getBoardLength(self)->float:
        """
        Vrátí potřebnou délku tránku, tak aby šla krokev vyřezat.
        @return: float
        """
        run_ratio = self.getRatio()[1]
        run = self.sirka_krokve
        rise = round((run/run_ratio),1)        
        result = round(self.getRafterLength()+self.getOverhang()+rise,2)
        return result

    def getTotalRafterLength(self)->float:
        """
        Vrátí celkovou délku krokve s přesahem.
        @return: float
        """
        result = round(self.getRafterLength()+self.getOverhang(),2)
        return result

    def getDegrees(self)->dict:
        """
        Vrátí tabulku stoupání s převodem na stupně.
        @return: dict
        """
        seznam = {"1:12":"4.76",
                  "2:12":"9.46",
                  "3:12":"14.04",
                  "4:12":"18.43",
                  "5:12":"22.62",
                  "6:12":"26.57",
                  "7:12":"30.26",
                  "8:12":"33.69",
                  "9:12":"36.87",
                  "10:12":"39.81",
                  "11:12":"42.51",
                  "12:12":"45",
                  "13:12":"47.29",
                  "14:12":"49.4",
                  "15:12":"51.34",
                 }
        return seznam
