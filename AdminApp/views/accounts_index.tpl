<!DOCTYPE html>

<html>
  
  <head>
    <title>Accounts</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>
  </head>

  <body>
  <h3>Accounts</h3>
 %if len(accounts_total)>0:
 <table>
 <thead>
 <tr>
 <th></th>
 <th>Today</th>
 <th>Yesterday</th>
 <th>This Month</th>
 <th>Total</th>
 </tr>
 </thead>
 <tbody>
 %for account in accounts_total:
 <tr>
 


 <td><a href='/account_view/{{accounts_url[account]}}'>{{account}}</a></td>
 <td>
 %if account in accounts_today:
 {{accounts_today[account]}}
 %else:
 0
 %end
 </td>
 <td>
 %if account in accounts_yesterday:
 {{accounts_yesterday[account]}}
 %else:
 0
 %end
 </td>
 <td>
 %if account in accounts_month:
 {{accounts_month[account]}}
 %else:
 0
 %end
 </td>
 <td>{{accounts_total[account]}}</td>
 </tr>
 %end
 </tbody>
 </table>
 %end
 
  </body>

</html>