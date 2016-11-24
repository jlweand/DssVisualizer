package datacreator;

public class KeyPress {
	
	private int keypress_id;
	private String content;
	private String classname;
	private String start;

	public KeyPress(){
	}
	
	public KeyPress(int keypress_id, String content, String classname, String start){
		this.setKeypress_id(keypress_id);
		this.content = content;
		this.classname = classname;
		this.start = start;
	}
	
	public int getKeypress_id() {
		return keypress_id;
	}

	public void setKeypress_id(int keypress_id) {
		this.keypress_id = keypress_id;
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

	public String getClassname() {
		return classname;
	}

	public void setClassname(String classname) {
		this.classname = classname;
	}

	public String getStart() {
		return start;
	}

	public void setStart(String start) {
		this.start = start;
	}

}


