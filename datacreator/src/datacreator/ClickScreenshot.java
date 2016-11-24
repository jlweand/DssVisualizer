package datacreator;

public class ClickScreenshot extends Screenshot {

	private int clicks_id;

	public ClickScreenshot() {
	}

	public ClickScreenshot(int clicks_id, String content, String type, String classname, String title, String comment, String start) {
		super(content, type, classname, title, comment, start);
		this.clicks_id = clicks_id;
	}

	public int getClicks_id() {
		return clicks_id;
	}

	public void setClicks_id(int clicks_id) {
		this.clicks_id = clicks_id;
	}

}
