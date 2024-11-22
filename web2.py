import streamlit as st
import math

def Tran_Eff(VSC, ISC, WSC):
    ZSC = VSC / ISC
    R1 = WSC / (ISC ** 2)
    X1 = math.sqrt(ZSC ** 2 - R1 ** 2)
    return R1, X1

def main():
    st.title("2305A21L01-PS-8")
    
    st.header("calculate the winding resistance and reactance of a transformer based on short circuit test")
    
    

    
    st.title("input parameters")
    VSC = st.number_input("Enter VSC (in Volts)", min_value=0.0)
    ISC = st.number_input("Enter ISC (in Amperes)", min_value=0.0)
    WSC = st.number_input("Enter WSC (in Watts)", min_value=0.0)
    
    if st.button("Calculate"):
        st.title("output parameters")
        R1, X1 = Tran_Eff(VSC, ISC, WSC)
        st.write(f"R1 (Winding Resistance): {R1:.4f} Ohms")
        st.write(f"X1 (Reactance): {X1:.4f} Ohms")
        

if __name__ == "__main__":
    main()
