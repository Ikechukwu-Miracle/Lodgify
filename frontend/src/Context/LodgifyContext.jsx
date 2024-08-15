import React, { createContext, useState } from 'react';
import inspirationListing from '../Components/Assets/footer-inspiration';

export const LodgifyContext = createContext(null);

const LodgeContextProvider = (props) => {
    const contextValue = {inspirationListing}
    return (
        <LodgifyContext.Provider value={contextValue}>
            {props.children}
        </LodgifyContext.Provider>
  )
}

export default LodgeContextProvider;