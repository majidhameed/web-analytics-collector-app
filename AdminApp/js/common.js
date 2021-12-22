function log(msg,mode='debug') {
	switch(mode) {
		case 'info':
			console.info(msg);
			break;
		case 'debug':
			console.debug(msg);
			break;
		case 'error':
			console.error(msg);
			break;
		default:
			console.debug(msg);
			break;		
	}
}