package org.biodig.images;
import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;
//Ancient Class Not being used
public class JerseyGetMetaImage {
	public static void main(String[] args) {
		try {
			Client client = Client.create();
			WebResource webResource = client.resource("http://10.34.229.145/api/tagGroups/search");
			ClientResponse response = webResource.accept("application/json").get(ClientResponse.class);
			
			if (response.getStatus() != 200) {
				throw new RuntimeException("Failed: HTTP error code : " + response.getStatus());
			}
			
			String output = response.getEntity(String.class);
			
			System.out.println("Output from Server ... \n");
			System.out.println(output);
			
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
