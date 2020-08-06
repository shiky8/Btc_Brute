import blocksmith
address_1 = str(input('Enter the btc address: ')) #'1PQc5NNSdvRwyw2RvrrQcBF4jHnmQFRkaL'
sert=0
while True:    
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890') # paddress_1aphrase
    private_Key = paddress_1aphrase.generate_key()
    address = blocksmith.BitcoinWallet.generate_address(private_Key)
    sert+=1
    if address_1 == address:
        print("we found it ")
        print("private private_Key = ", private_Key)
        print("address = ",address)
        break
    else:
        print("trying private private_Key = ", private_Key)
        print("address = ",address)
        continue 
