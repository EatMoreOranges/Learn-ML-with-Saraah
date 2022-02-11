    if state == "t":
        #### for training the model
        naMeanings = [
            "LotFrontage","Alley","MasVnrType","BsmtQual","BsmtCond","BsmtExposure","BsmtFinType1","BsmtFinType2","FireplaceQu",
            "GarageType","GarageYrBlt","GarageFinish","GarageQual","GarageCond","PoolQC","Fence","MiscFeature"] 
        
        for col in naMeanings:
            if col == "LotFrontage":
                df['LotFrontage'].fillna(value=df['LotFrontage'].mean(), inplace=True)
            elif col == 'GarageYrBlt':
                # df['GarageYrBlt'].fillna(value=0, inplace=True)
                checks['GarageYrBlt'].fillna(value=checks['GarageYrBlt'].mean(), inplace=True)
            else:
                df[col].fillna("notIncluded", inplace=True)
                # df[col].fillna(0, inplace=True)
    
        # df.dropna(axis=0, inplace = True) 
        df["MasVnrArea"].fillna(value=df['MasVnrArea'].mean(), inplace=True)
    else:
        ### for predicting with the model
        naMeanings = ["LotFrontage","Alley","MasVnrType","BsmtQual","BsmtCond","BsmtExposure","BsmtFinType1","BsmtFinType2","FireplaceQu",
        "GarageType","GarageYrBlt","GarageFinish","GarageQual","GarageCond","PoolQC","Fence","MiscFeature"] 
    
        for col in naMeanings:
            if col == "LotFrontage":
                df['LotFrontage'].fillna(value=df['LotFrontage'].mean(), inplace=True)
            elif col == 'GarageYrBlt':
                # df['GarageYrBlt'].fillna(value=0, inplace=True)
                checks['GarageYrBlt'].fillna(value=checks['GarageYrBlt'].mean(), inplace=True)
            else:
                df[col].fillna("notIncluded", inplace=True)
                # df[col].fillna(0, inplace=True)

        ### df.dropna(axis=0, inplace = True) 
        df["MasVnrArea"].fillna(value=df['MasVnrArea'].mean(), inplace=True)