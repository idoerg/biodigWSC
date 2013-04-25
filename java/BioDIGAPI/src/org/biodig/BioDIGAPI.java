package org.biodig;

public class BioDIGAPI {
	
	/**
	 * 
	 * Creates an instance of the BioDIG API for the given web address
	 * 
	 * @param address The web address of the server's REST API for the requests to be made. 
	 * If your BioDIG instance is running at http://example.org/ then you would pass in 
	 * http://example.org/api/ for standard installs.
	 */
	public BioDIGAPI(String address) {
		// TODO instantiation code
	}
	
	/**
	 * Gets a tag from the server using its id. 
	 * 
	 * @param id The unique identifier of the tag in the BioDIG system.
	 * @return A tag object representing the tag retrieved
	 */
	public Tag getTag(int id) throws NotFoundException {
		
	}
	
	/**
	 * Creates a new tag on the server and returns the tag object that was created
	 * 
	 * @param query
	 * @return
	 */
	public Tag createTag(TagQuery query) {
		
	}
}
