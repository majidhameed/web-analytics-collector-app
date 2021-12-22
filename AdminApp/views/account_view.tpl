% include('header.tpl', title="Account View")
  <h2>{{website}}</h2>
  <input type="hidden" id="website" name="website" value="{{website}}" />
  From:<input type="date" id="from_date" name="from_date" title="MM/DD/YYYY" required />
  To:<input type="date" id="to_date" name="to_date" title="MM/DD/YYYY" />
  <button type="button" class="btn btn-xs btn-default" id="by_date_btn" name="by_date_btn">Update</button>
  <div id="date_hits" class="lead"></div>
<script>
$(function(){
$('#from_date').datepicker();
$('#to_date').datepicker();
});

$('#by_date_btn').click(function(){
	var from_date = $('#from_date').val();
	var to_date = $('#to_date').val();
	var website = $('#website').val();
	$.post('/accounts_by_date_range',{'from_date':from_date,'to_date':to_date, 'website':website},function(response){
	log(response);
	$('#date_hits').text(response[website]);
	});
});


</script>
% include('footer.tpl')