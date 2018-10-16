import csv

with  open('data.csv',mode='w') as csv_file:

    fieldnames=['Alt','Bar','Fri','Hun','Pat','Price','Rain','Res','Type','Est','Goal']
    writer = csv.DictWriter(csv_file,fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({'Alt':'Yes','Bar':'No','Fri':'No','Hun':'Yes','Pat':'Some','Price':'100','Rain':'No','Res':'Yes','Type':'French','Est':'0-10','Goal':'Yes'})
    writer.writerow({'Alt':'Yes','Bar':'No','Fri':'No','Hun':'Yes','Pat':'Full','Price':'10','Rain':'No','Res':'No','Type':'Thai','Est':'30-60','Goal':'NO'})
    writer.writerow({'Alt':'No','Bar':'Yes','Fri':'No','Hun':'No','Pat':'Some','Price':'10','Rain':'No','Res':'No','Type':'Burger','Est':'0-10','Goal':'Yes'})
    writer.writerow({'Alt':'Yes','Bar':'No','Fri':'Yes','Hun':'Yes','Pat':'Full','Price':'10','Rain':'Yes','Res':'No','Type':'Thai','Est':'10-30','Goal':'Yes'})
    writer.writerow({'Alt':'Yes','Bar':'No','Fri':'Yes','Hun':'No','Pat':'Full','Price':'100','Rain':'No','Res':'Yes','Type':'French','Est':'>60','Goal':'No'})
    writer.writerow({'Alt':'No','Bar':'Yes','Fri':'No','Hun':'Yes','Pat':'Some','Price':'75','Rain':'Yes','Res':'Yes','Type':'Italian','Est':'0-10','Goal':'Yes'})
    writer.writerow({'Alt':'No','Bar':'Yes','Fri':'No','Hun':'No','Pat':'None','Price':'10','Rain':'Yes','Res':'No','Type':'Burger','Est':'0-10','Goal':'No'})
    writer.writerow({'Alt':'No','Bar':'No','Fri':'No','Hun':'Yes','Pat':'Some','Price':'75','Rain':'Yes','Res':'Yes','Type':'Thai','Est':'0-10','Goal':'Yes'})
    writer.writerow({'Alt':'No','Bar':'Yes','Fri':'Yes','Hun':'No','Pat':'Full','Price':'10','Rain':'Yes','Res':'No','Type':'Burger','Est':'>60','Goal':'No'})
    writer.writerow({'Alt':'Yes','Bar':'Yes','Fri':'Yes','Hun':'Yes','Pat':'Full','Price':'100','Rain':'No','Res':'Yes','Type':'Italian','Est':'10-30','Goal':'No'})
    writer.writerow({'Alt':'No','Bar':'No','Fri':'No','Hun':'No','Pat':'None','Price':'10','Rain':'No','Res':'No','Type':'Thai','Est':'0-10','Goal':'No'})
    writer.writerow({'Alt':'Yes','Bar':'Yes','Fri':'Yes','Hun':'Yes','Pat':'Full','Price':'10','Rain':'No','Res':'No','Type':'Burger','Est':'30-60','Goal':''})